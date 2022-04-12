# Copyright (c) 2016-2022 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import logging
import re

from html import escape
from html.parser import HTMLParser
from mkdocs.commands.build import DuplicateFilter
from mkdocs.contrib.search import SearchPlugin as BasePlugin
from mkdocs.contrib.search.search_index import SearchIndex as BaseIndex

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Search plugin with custom search index
class SearchPlugin(BasePlugin):

    # Override: use custom search index
    def on_pre_build(self, config):
        options = { "tags": "tags" in config["plugins"] }
        self.search_index = SearchIndex(**self.config, **options)
        if self.config["prebuild_index"]:
            log.warning(
                "Material for MkDocs doesn't support the 'prebuild_index' "
                "option. Please remove it from 'mkdocs.yml'."
            )

            # Set to false, just to be sure
            self.config["prebuild_index"] = False

    # Override: remove search pragmas after indexing
    def on_page_context(self, context, page, **kwargs):
        self.search_index.add_entry_from_context(context["page"])
        page.content = re.sub(
            r'\s?data-search-\w+="[^"]+"',
            "",
            page.content
        )

# -----------------------------------------------------------------------------

# Search index with support for additional fields
class SearchIndex(BaseIndex):

    # Override: use custom content parser
    def add_entry_from_context(self, page):
        search = page.meta.get("search", {})
        if "exclude" in search and search["exclude"]:
            return

        # Divide page content into sections
        parser = Parser()
        parser.feed(page.content)
        parser.close()

        # Add sections to index
        for section in parser.data:
            if not section.is_excluded():
                self.create_entry_for_section(section, page.toc, page.url, page)

    # Override: graceful indexing and additional fields
    def create_entry_for_section(self, section, toc, url, page):
        item = self._find_toc_by_id(toc, section.id)
        if item:
            url = url + item.url
        elif section.id:
            url = url + f"#{section.id}"

        # Compute title and text
        title = "".join(section.title or page.title).strip()
        text  = "".join(section.text).strip()

        # Reset text, if only titles should be indexed
        if self.config["indexing"] == "titles":
            text = ""

        # Create entry for section
        entry = {
            "title": title,
            "text": text,
            "location": url
        }

        # Add document tags, if any
        if self.config["tags"] and "tags" in page.meta:
            if type(page.meta["tags"]) is list:
                entry["tags"] = page.meta["tags"]
            else:
                log.warning(
                    "Skipping 'tags' due to invalid syntax [%s]: %s",
                    page.file.src_path,
                    page.meta["tags"]
                )

        # Add document boost for search, if any
        search = page.meta.get("search", {})
        if "boost" in search:
            entry["boost"] = search["boost"]

        # Add entry to index
        self._entries.append(entry)

# -----------------------------------------------------------------------------

# HTML element
class Element:
    """
    An element with attributes, essentially a small wrapper object for the
    parser to access attributes in other callbacks than handle_starttag.
    """

    # Initialize HTML element
    def __init__(self, tag, attrs = dict()):
        self.tag   = tag
        self.attrs = attrs

    # Support comparison (compare by tag only)
    def __eq__(self, other):
        if other is Element:
            return self.tag == other.tag
        else:
            return self.tag == other

    # Support set operations
    def __hash__(self):
        return hash(self.tag)

    # Check whether the element should be excluded
    def is_excluded(self):
        if "data-search-exclude" in self.attrs:
            return True

        # Element is not excluded
        return False

# -----------------------------------------------------------------------------

# HTML section
class Section:
    """
    A block of text with markup, preceded by a title (with markup), i.e., a
    headline with a certain level (h1-h6). Internally used by the parser.
    """

    # Initialize HTML section
    def __init__(self, el):
        self.el    = el
        self.text  = []
        self.title = []
        self.id = None

    # Check whether the section should be excluded
    def is_excluded(self):
        return self.el.is_excluded()

# -----------------------------------------------------------------------------

# HTML parser
class Parser(HTMLParser):
    """
    This parser divides the given string of HTML into a list of sections, each
    of which are preceded by a h1-h6 level heading. A white- and blacklist of
    tags dictates which tags should be preserved as part of the index, and
    which should be ignored in its entirety.
    """

    # Initialize HTML parser
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tags to skip
        self.skip = set([
            "object",                  # Objects
            "script",                  # Scripts
            "style"                    # Styles
        ])

        # Tags to keep
        self.keep = set([
            "p",                       # Paragraphs
            "code", "pre",             # Code blocks
            "li", "ol", "ul"           # Lists
        ])

        # Current context and section
        self.context = []
        self.section = None

        # All parsed sections
        self.data = []

    # Called at the start of every HTML tag
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        # Ignore self-closing tags
        el = Element(tag, attrs)
        if not tag in void:
            self.context.append(el)
        else:
            return

        # Handle headings
        if tag in ([f"h{x}" for x in range(1, 7)]):
            if "id" in attrs:

                # Ensure top-level section
                if tag != "h1" and not self.data:
                    self.section = Section(Element("hx"))
                    self.data.append(self.section)

                # Set identifier, if not first section
                self.section = Section(el)
                if self.data:
                    self.section.id = attrs["id"]

                # Append section to list
                self.data.append(self.section)

        # Handle preface - ensure top-level section
        if not self.section:
            self.section = Section(Element("hx"))
            self.data.append(self.section)

        # Handle special cases to skip
        for key, value in attrs.items():

            # Skip block if explicitly excluded from search
            if key == "data-search-exclude":
                self.skip.add(el)
                return

            # Skip line numbers, see https://bit.ly/3GvubZx
            if key == "class" and value == "linenodiv":
                self.skip.add(el)
                return

        # Render opening tag if kept
        if not self.skip.intersection(self.context):
            if tag in self.keep:
                data = self.section.text
                if self.section.el in reversed(self.context):
                    data = self.section.title

                # Append to section title or text
                data.append(f"<{tag}>")

    # Called at the end of every HTML tag
    def handle_endtag(self, tag):
        if not self.context or self.context[-1] != tag:
            return

        # Remove element from skip list
        el = self.context.pop()
        if el in self.skip:
            self.skip.remove(el)
            return

        # Render closing tag if kept
        if not self.skip.intersection(self.context):
            if tag in self.keep:
                data = self.section.text
                if self.section.el in reversed(self.context):
                    data = self.section.title

                # Append to section title or text
                data.append(f"</{tag}>")

    # Called for the text contents of each tag
    def handle_data(self, data):
        if self.skip.intersection(self.context):
            return

        # Collapse whitespace in non-pre contexts
        if not "pre" in self.context:
            if not data.isspace():
                data = data.replace("\n", " ")
            else:
                data = " "

        # Handle preface - ensure top-level section
        if not self.section:
            self.section = Section(Element("hx"))
            self.data.append(self.section)

        # Handle section headline
        if self.section.el in reversed(self.context):
            permalink = False
            for el in self.context:
                if el.tag == "a" and el.attrs.get("class") == "headerlink":
                    permalink = True

            # Ignore permalinks
            if not permalink:
                self.section.title.append(
                    escape(data, quote = False)
                )

        # Handle everything else
        else:
            self.section.text.append(
                escape(data, quote = False)
            )

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())

# Tags that are self-closing
void = set([
    "area",                    # Image map areas
    "base",                    # Document base
    "br",                      # Line breaks
    "col",                     # Table columns
    "embed",                   # External content
    "hr",                      # Horizontal rules
    "img",                     # Images
    "input",                   # Input fields
    "link",                    # Links
    "meta",                    # Metadata
    "param",                   # External parameters
    "source",                  # Image source sets
    "track",                   # Text track
    "wbr"                      # Line break opportunities
])
