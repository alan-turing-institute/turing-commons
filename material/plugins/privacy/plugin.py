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
import os
import posixpath
import re
import requests

from fnmatch import fnmatch
from lxml import html
from mkdocs import utils
from mkdocs.commands.build import DuplicateFilter
from mkdocs.config.config_options import Choice, Deprecated, Type
from mkdocs.plugins import BasePlugin
from shutil import copyfile
from urllib.parse import urlparse

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Privacy plugin
class PrivacyPlugin(BasePlugin):

    # Configuration scheme
    config_scheme = (
        ("enabled", Type(bool, default = True)),

        # Options for external assets
        ("externals", Choice(("bundle", "report"), default = "bundle")),
        ("externals_directory", Type(str, default = "assets/externals")),
        ("externals_exclude", Type(list, default = [])),

        # Deprecated options
        ("download", Deprecated(moved_to = "enabled")),
        ("download_directory", Deprecated(moved_to = "externals_directory")),
    )

    # Determine base and initialize resource mappings
    def on_config(self, config):
        self.base_url = urlparse(config.get("site_url"))
        self.base_dir = config.get("site_dir")
        self.resource = dict()
        self.files = []

    # Determine files that need to be post-processed
    def on_files(self, files, config):
        if not self.config.get("enabled"):
            return

        # Filter relevant files, short-circuit lunr.js
        for file in files:
            if file.url.endswith(".js") or file.url.endswith(".css"):
                if not "assets/javascripts/lunr" in file.url:
                    self.files.append(file)

        # If site URL is not given, add Mermaid.js - see https://bit.ly/36tZXsA
        # This is a special case, as Material for MkDocs automatically loads
        # Mermaid.js when a Mermaid diagram is found in the page.
        if not config.get("site_url"):
            if not any("mermaid" in js for js in config["extra_javascript"]):
                config["extra_javascript"].append(
                    "https://unpkg.com/mermaid@8.13.3/dist/mermaid.min.js"
                )

    # Parse, fetch and store external assets in pages
    def on_post_page(self, output, page, config):
        if not self.config.get("enabled"):
            return

        # Find all external scripts and style sheets
        expr = re.compile(
            r'<(?:link[^>]+href?|script[^>]+src)=[\'"]?http[^>]+>',
            re.IGNORECASE | re.MULTILINE
        )

        # Parse occurrences and replace in reverse
        for match in reversed(list(expr.finditer(output))):
            value = match.group()

            # Compute offsets for replacements
            l = match.start()
            r = l + len(value)

            # Handle preconnect hints and style sheets
            el = html.fragment_fromstring(value)
            if el.tag == "link":
                raw = el.get("href", "")

                # Check if URL is external
                url = urlparse(raw)
                if not self.__is_external(url):
                    continue

                # Replace external preconnect hint in output
                rel = el.get("rel")
                if rel == "preconnect":
                    output = output[0:l] + output[r:]

                # Replace external style sheet in output
                if rel == "stylesheet":
                    output = "".join([
                        output[:l],
                        value.replace(raw, self.__fetch(url, page)),
                        output[r:]
                    ])

            # Handle external scripts
            if el.tag == "script":
                raw = el.get("src", "")

                # Check if URL is external
                url = urlparse(raw)
                if not self.__is_external(url):
                    continue

                # Replace external script in output
                output = "".join([
                    output[:l],
                    value.replace(raw, self.__fetch(url, page)),
                    output[r:]
                ])

        # Return output with replaced occurrences
        return output

    # Parse, fetch and store external assets in assets
    def on_post_build(self, config):
        if not self.config.get("enabled"):
            return

        # Check all files that are part of the build
        for file in self.files:
            path = os.path.join(self.base_dir, file.dest_path)
            if not os.path.isfile(path):
                continue

            # Handle internal style sheet or script
            if path.endswith(".css") or path.endswith(".js"):
                with open(path, encoding = "utf-8") as f:
                    utils.write_file(
                        self.__fetch_dependents(f.read(), file.dest_path),
                        path
                    )

    # -------------------------------------------------------------------------

    # Check if the given URL is external
    def __is_external(self, url):
        return url.hostname != self.base_url.hostname

    # Check if the given URL is excluded
    def __is_excluded(self, url, base):
        url = re.sub(r'^https?:\/\/', "", url)
        for pattern in self.config.get("externals_exclude"):
            if fnmatch(url, pattern):
                log.debug(f"Excluded asset in '{base}': {url}")
                return True

        # Exclude all external assets if bundling is not enabled
        if self.config.get("externals") == "report":
            log.warning(f"External asset in '{base}': {url}")
            return True

    # Fetch external resource in given page
    def __fetch(self, url, page):
        raw = url.geturl()

        # Check if URL is excluded
        if self.__is_excluded(raw, page.file.dest_path):
            return raw

        # Fetch external asset for bundling
        if not url in self.resource:
            res = requests.get(raw, headers = {

                # Set user agent explicitly, so Google Fonts gives us *.woff2
                # files, which according to caniuse.com is the only format we
                # need to download as it covers the entire range of browsers
                # we're officially supporting
                "User-Agent": " ".join([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "AppleWebKit/537.36 (KHTML, like Gecko)",
                    "Chrome/98.0.4758.102 Safari/537.36"
                ])
            })

            # Compute path name after cleaning up URL
            data = url._replace(scheme = "", query = "", fragment = "")
            file = os.path.join(
                self.config.get("externals_directory"),
                data.geturl()[2:]
            )

            # Compute and ensure presence of file extension
            name = re.findall(r'^[^;]+', res.headers["content-type"])[0]
            extension = extensions[name]
            if not file.endswith(extension):
                file += extension

            # Compute and post-process content
            content = res.content
            if extension == ".css" or extension == ".js":
                content = self.__fetch_dependents(res.text, file)

            # Write content to file
            utils.write_file(content, os.path.join(
                self.base_dir,
                file
            ))

            # Update resource mappings
            self.resource[url] = file

        # Return URL relative to current page
        return utils.get_relative_url(
            utils.normalize_url(self.resource[url]),
            page.url
        )

    # Fetch dependent resources in external assets
    def __fetch_dependents(self, output, base):

        # Fetch external assets in style sheet
        if base.endswith(".css"):
            expr = re.compile(
                r'url\((\s*http?[^)]+)\)',
                re.IGNORECASE | re.MULTILINE
            )

        # Fetch external assets in script
        elif base.endswith(".js"):
            expr = re.compile(
                r'["\'](http[^"\']+\.js)["\']',
                re.IGNORECASE | re.MULTILINE
            )

        # Parse occurrences and replace in reverse
        for match in reversed(list(expr.finditer(output))):
            value = match.group(0)
            raw   = match.group(1)

            # Compute offsets for replacements
            l = match.start()
            r = l + len(value)

            # Check if URL is external
            url = urlparse(raw)
            if not self.__is_external(url):
                continue

            # Check if URL is excluded
            if self.__is_excluded(raw, base):
                continue

            # Download file if it's not contained in the cache
            data = url._replace(scheme = "", query = "", fragment = "")
            file = os.path.join(".cache", data.geturl()[2:])
            if not os.path.isfile(file):
                res = requests.get(raw)
                utils.write_file(res.content, file)

            # Compute final path relative to output directory
            path = os.path.join(
                self.config.get("externals_directory"),
                data.geturl()[2:]
            )

            # Create relative URL for asset in style sheet
            if base.endswith(".css"):
                url = utils.get_relative_url(path, base)

            # Create absolute URL for asset in script
            elif base.endswith(".js"):
                url = posixpath.join(self.base_url.geturl(), path)

            # Replace external asset in output
            output = "".join([
                output[:l],
                value.replace(raw, url),
                output[r:]
            ])

            # Ensure presence of directory
            path = os.path.join(self.base_dir, path)
            directory = os.path.dirname(path)
            if not os.path.isdir(directory):
                os.makedirs(directory)

            # Copy file from cache
            copyfile(file, path)

        # Return output with replaced occurrences
        return bytes(output, encoding = "utf8")

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())

# Expected file extensions
extensions = dict({
    "application/javascript": ".js",
    "text/javascript": ".js",
    "text/css": ".css"
})
