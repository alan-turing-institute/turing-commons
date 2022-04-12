# Contributing to _The Turing Commons_

:tada::balloon::smile: **Welcome to _The Turing Commons_ repository!** :smile::balloon::tada:

We hope that the information provided in this document will make it as easy as possible for you to get involved.

Primarily, this repository exists to support a series of online courses on the topics of Responsible Research and Innovation (RRI), AI Ethics & Governance (AEG), and Public Communication of Science (PCS). However, you will also find a variety of tools and resources that can be used for whatever purpose you believe they could be useful for.

We welcome all contributions to this project via GitHub issues and pull requests. Please follow these guidelines to make sure your contributions can be easily integrated into the projects. 

If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](#get-in-touch).

## Table of contents

Been here before? Already know what you're looking for in this guide? Jump to the following sections:

- [Contributing to _The Turing Commons_](#contributing-to-the-turing-commons)
  - [Table of contents](#table-of-contents)
  - [Inclusivity](#inclusivity)
  - [Get in touch](#get-in-touch)
  - [Contributing through GitHub](#contributing-through-github)
  - [Writing in Markdown](#writing-in-markdown)
  - [Where to start: issues](#where-to-start-issues)
  - [Making a change with a pull request](#making-a-change-with-a-pull-request)
    - [1. Comment on an existing issue or open a new issue referencing your addition](#1-comment-on-an-existing-issue-or-open-a-new-issue-referencing-your-addition)
    - [2. Fork](#2-fork-the-turing-commons-repositoryturing-commons-repo)
    - [3. Make the changes you've discussed](#3-make-the-changes-youve-discussed)
    - [4. Submit a pull request](#4-submit-a-pull-request)
  - [Recognising Contributions](#recognising-contributions)

## Inclusivity

_The Turing Commons_ aims to be inclusive to people from all walks of life and to all research fields. These intentions must be reflected in the contributions that we make to the project.

We encourage intentional, inclusive actions from contributors. Here are a few examples of such actions:

- use respectful, gender-neutral and inclusive language (learn more about inclusive writing on page 22 of [University of Leicester Study Skills pdf](https://www2.le.ac.uk/projects/oer/oers/ssds/oers/study-skills/studyskills.pdf), also available as a [zipped html](https://www2.le.ac.uk/projects/oer/oers/ssds/oers/study-skills/studyskills_HTML.zip)).
- aim to include perspectives of researchers from different research backgrounds such as science, humanities and social sciences by not limiting the scope to only scientific domains.
- make sure that the colour palettes are accessible to colour-blind readers and contributors.
See the blogpost [Designing Scientific Figures for Colour Blindness](https://www.lewismackenzie.science/blog-1/2017/2/9/designing-scientific-figures-for-colour-blindness) for an example of how somebody improved one of their diagrams, including links to recommended colour palettes and a colour-blindness simulator.

## Get in touch

To get in touch with _The Turing Commons_ team, you can use the following options:

- GitHub [issues](turing-commons-issues) and [pull requests](https://github.com/chrisdburr/turing-commons/pulls)
  - Join a discussion, collaborate one an ongoing task and exchange your thoughts with others.
  - Can't find your idea being discussed anywhere?
    [Open a new issue](https://github.com/chrisdburr/turing-commons/issues/new)! (See our [Where to start: issues](#where-to-start-issues) section below.)
- Contact the Project Lead of _The Turing Commons_ project - Christopher Burr - by email at [cburr@turing.ac.uk](mailto:cburr@turing.ac.uk).

## Contributing through GitHub

[Git][git] is a really useful tool for version control.
[GitHub][github] sits on top of Git and supports collaborative and distributed working.

In order to contribute via GitHub, you'll need to set up a free account and sign in.
Here are some [instructions](https://help.github.com/articles/signing-up-for-a-new-github-account/) to help you get going.

## Writing in Markdown

GitHub has a helpful page on [getting started with writing and formatting on GitHub](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github).

Most of the writing that you'll do will be in [Markdown][markdown].
You can think of Markdown as a few little symbols around your text that will allow GitHub to render the text with a little bit of formatting.
For example, you could write words as **bold** (`**bold**`), or in _italics_ (`_italics_`), or as a [link][[rick-roll](https://youtu.be/dQw4w9WgXcQ)] (`[link](https://youtu.be/dQw4w9WgXcQ)`) to another webpage.

<!-- When writing in Markdown, please start each new sentence on a new line.
Having each sentence on a new line will make no difference to how the text is displayed, there will still be paragraphs, but it makes the [diffs produced during the pull request](https://help.github.com/en/articles/about-comparing-branches-in-pull-requests) review easier to read! :sparkles: -->

## Where to start: issues

Before you open a new issue, please check if any of our [open issues](https://github.com/chrisdburr/turing-commons/issues) cover your idea already.
If you open a new issue, please follow our basic guidelines laid out in our [issue templates](https://github.com/chrisdburr/turing-commons/issues/new).
There are 2 issues templates to choose from:
1. General ([preview here](https://github.com/alan-turing-institute/the-turing-way/issues/new?assignees=&template=ISSUE_TEMPLATE.md)):  Use this template for a general issue related to the book, community, process or ideas.
2. Bug Report ([preview here](https://github.com/alan-turing-institute/the-turing-way/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D)): With this template, create an issue report that can help others repair something that is currently broken.
This can be used for reporting errors like typos and broken links.
The issue template will automatically be rendered in the comment section of the new issue page, so all you need to do is edit the "_Lorem ipsum_" sections.

<!-- ### Issue labels

The list of labels for current issues can be found [here][turing-way-labels] and includes:

- [![approval-request](https://img.shields.io/badge/-approval%20request-8bd82d.svg)][labels-approval-request] _When a bug or minor changes have been made, contributors can label their PR along with "bug fixed"._

- [![binderhub](https://img.shields.io/badge/-binderhub-F37726.svg)][labels-binderhub] _These issues relate to documentation and resources around building a BinderHub._

- [![book-build](https://img.shields.io/badge/-book--build-8d7aef.svg)][labels-book-build] _These issues are related to the build of the book using Jupyter-book. They are also related to the-turing-way book repo._

- [![book-dash-feb20](https://img.shields.io/badge/-book--dash--feb20-006b75.svg)][labels-book-dash-feb20] _These are to be used on issues and PR during/for the book dash in Feb 2020._

- [![book-dash-ldn19](https://img.shields.io/badge/-book--dash--ldn19-e0b61f.svg)][labels-book-dash-ldn19] _These are issues related to contributions made during the London Book Dash in 2019._

- [![book-dash-mcr19](https://img.shields.io/badge/-book--dash--mcr19-f2a9c1.svg)][labels-book-dash-mcr19] _These are issues related to contributions made during the Manchester Book Dash in 2019._

- [![Bug](https://img.shields.io/badge/-bug-d73a4a.svg)][labels-bug] _These issues are reporting a problem or a mistake in the project._

  The more details you can provide the better!
  If you know how to fix the bug, please open an issue first and then submit a pull request :sparkles:

- [![bug-fixed](https://img.shields.io/badge/-bug%20fixed-cef298.svg)][labels-bug-fixed] _These are bugs that have been fixed and only need approval._

- [![collaboration-book](https://img.shields.io/badge/-collaboration--book-c877ff.svg)][labels-collaboration-book] _These issues relate to the content of the collaboration book._

- [![Comms](https://img.shields.io/badge/-comms-15c4b2.svg)][labels-comms] _These issues discuss how we as a project interact with other initiatives._

- [![communication-book](https://img.shields.io/badge/-communication--book-52d8d8.svg)][labels-communication-book] _These issues relate to the content of the communication book._

- [![Community](https://img.shields.io/badge/-community-8605c1.svg)][labels-community] _These issues relate to building and supporting the Turing Way community._

  This is all about collaborating, so please let us know how we can best support you as a community member.

- [![conflicting-file-error](https://img.shields.io/badge/-conflicting--file--error-a00819.svg)][labels-conflicting-file-error] _These issues mark issues and pull requests with conflicting files and errors._

- [![dependencies](https://img.shields.io/badge/-dependencies-0366d6.svg)][labels-dependencies] _These issues relate to pull requests that update a dependency file._

- [![Enhancement](https://img.shields.io/badge/-enhancement-84b6eb.svg)][labels-enhancement] _These issues are suggesting new features that can be added to the project._

  If you want to ask for something new, please try to make sure that your request is distinct from any others that are already in the queue (or part of _The Turing Way_).
  If you find one that's similar but there are subtle differences please reference the other enhancement in your issue.

- [![ethics-book](https://img.shields.io/badge/-ethics--book-5e6fbc.svg)][labels-ethics-book] _These issues relate to the content of the ethics book._

- [![events](https://img.shields.io/badge/-events-100570.svg)][labels-events] _These issues relate to coordinating workshops, book dashes and any other events._

- [![good-first-issue](https://img.shields.io/badge/-good%20first%20issue-1b3487.svg)][labels-firstissue] _These issues are particularly appropriate if it is your first contribution to _The Turing Way_, or to GitHub overall._

  If you're not sure about how to go about contributing, these are good places to start. You'll be mentored through the process by the maintainers team.
  If you're a seasoned contributor, please select a different issue to work from and keep these available for the newer and potentially more anxious team members.

- [![help-wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][labels-helpwanted] _These issues contain a task that a member of the team has determined we need additional help with._

  If you feel that you can contribute to one of these issues, we especially encourage you to do so!

- [![idea-for-discussion](https://img.shields.io/badge/-idea--for--discussion-a2f29b.svg)][labels-idea-for-discussion] _These issues can be used for inviting discussion from collaborators or community in general._

- [![newsletter](https://img.shields.io/badge/-newsletter-81e2c4.svg)][labels-newsletter] _These issues contain items that can be added to the newsletter._

- [![outreach](https://img.shields.io/badge/-Outreach-fcbae8.svg)][labels-outreach] _These issues relate to topics to reach out to the community._

- [![good-first-PR-review](https://img.shields.io/badge/-good--first--PR--review-C992E0.svg)][labels-good-first-PR-review] _These pull requests are for the new members of _The Turing Way_ community who want to start with reviewing and approving some simple pull requests._

If you are a new member of _The Turing Way_ and are looking for opportunities to start as a reviewer of contributions made on our Github repository, these pull requests are a great starting point for you. Issues like small modifications, typo errors and minor bug fixes are resolved by these PRs which are easy to review as a beginner.

- [![pr-draft](https://img.shields.io/badge/-PR%3A%20draft-6a737d.svg)][labels-pr-draft] _These issues relate to draft pull requests._

- [![pr-merged](https://img.shields.io/badge/-PR%3A%20merged-6f42c1.svg)][labels-pr-merged] _These issues relate to pull requests that have been merged._

- [![pr-partially-approved](https://img.shields.io/badge/-PR%3A%20partially--approved-7E9C82.svg)][labels-pr-partially-approved] _These issues relate to pull requests that have been partially approved._

- [![pr-reviewed-approved](https://img.shields.io/badge/-PR%3A%20reviewed--approved-0e8a16.svg)][labels-pr-reviewed-approved] _These issues relate to pull requests that have been approved by a reviewer._

- [![pr-reviewed-changes-requested](https://img.shields.io/badge/-PR%3A%20reviewed--changes--requested-c2e0c6.svg)][labels-pr-reviewed-changes-requested] _These issues relate tp pull requests for which a reviewer has requested changes._

- [![pr-unreviewed](https://img.shields.io/badge/-PR%3A%20unreviewed-fbca04.svg)][labels-pr-unreviewed] _These issues relate to pull requests that have not been reviewed yet._

- [![project-design-book](https://img.shields.io/badge/-project--design--book-3982cc.svg)][labels-project-design-book] _These issues relate to the content of the project design book._

- [![project-management](https://img.shields.io/badge/-project%20management-bfd86c.svg)][labels-project-management] _We like to model best practice, so _The Turing Way_ itself is managed through these issues.
  These issues help us to coordinate some logistics._

- [![question](https://img.shields.io/badge/-question-cc317c.svg)][labels-question] _These issues contain a question that you'd like to have answered._

  There are [lots of ways to ask questions](#get-in-touch) but opening an issue is a great way to start a conversation and get your answer.

- [![ready-for-merge](https://img.shields.io/badge/-ready%20for%20merge-32a320.svg)][labels-ready-for-merge] _These issues can be used after approving a pull request to let the author know that they can merge it._

- [![reproducibility-book](https://img.shields.io/badge/-reproducibility--book-c5bcff.svg)][labels-reproducibility-book] _These issues relate to the content of the reproducibility book._

- [![research-related-theory](https://img.shields.io/badge/-research--related--theory-72dbff.svg)][labels-research-related-theory] _These issues relate to the theoretical side of research best practices._

- [![review-request](https://img.shields.io/badge/-review%20request-ed0602.svg)][labels-review-request] _These relate to pull requests for urgent review requests, for example, to approve a report, abstract, and newsletter._

- [![software-skills](https://img.shields.io/badge/-software--skills-ed886f.svg)][labels-software-skills] _These relate to issues and pull requests that may need some software development, design, or troubleshooting skills._

- [![Tools](https://img.shields.io/badge/-tools-a3e07d.svg)][labels-tools] _These issues discuss the tools we use for collaboration_

  If you feel that we should try new tools or some aspects of the collaboration could be improved by using tools, please let us know.

- [![translation](https://img.shields.io/badge/-translation-e1ed3d.svg)][labels-translation] _These issues relate to translating the reproducibility book into other languages._

- [![Travel](https://img.shields.io/badge/-travel-0f42fc.svg)][labels-travel] _These issues are mainly for the attention of core project members to plan travel to face to face meetings_

- [![typo-fix](https://img.shields.io/badge/-typo--fix-ff54d4.svg)][labels-typo-fix] _These issues relate to fixing typos and broken links._

- [![work-in-progress](https://img.shields.io/badge/-work--in--progress-e08f72.svg)][labels-work-in-progress] _These issues are work in progress._ -->

## Making a change with a pull request

We appreciate all contributions to _The Turing Commons_.
The following steps are a guide to help you contribute in a way that will be easy for everyone to review and accept with ease :sunglasses:.

### 1. Comment on an [existing issue](https://github.com/chrisdburr/turing-commons/issues) or open a new issue referencing your addition

This allows other members of _The Turing Commons_ team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

<!-- [This blog](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) is a nice explanation of why putting this work in upfront is so useful to everyone involved. -->

Remember, if you open a new issue, please follow our basic guidelines laid out in our [issue template](https://github.com/chrisdburr/turing-commons/master/.github/ISSUE_TEMPLATE/ISSUE_TEMPLATE.md).
The issue template will automatically be rendered in the comment section of the new issue page so all you need to do is edit the "_Lorem ipsum_" sections.

### 2. [Fork][github-fork] [_The Turing Commons_ repository][turing-commons-repo]

This is now your own unique copy of _The Turing Commons_.
Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!

Make sure to [keep your fork up to date][github-syncfork] with the master repository, otherwise, you can end up with lots of dreaded [merge conflicts][github-mergeconflicts].
If you prefer working in the browser, [these instructions](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser) describe how to sync your fork to the original repository via GitHub.

### 3. Make the changes you've discussed

Try to keep the changes focused.
If you submit a large amount of work all in one go it will be much more work for whoever is reviewing your pull request.

While making your changes, commit often and write good, detailed commit messages.
[This blog](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.

If you feel tempted to "branch out" then please make a [new branch][github-branches] and a [new issue][turing-commons-issues] to go with it. [This blog](https://nvie.com/posts/a-successful-git-branching-model/) details the different Git branching models.

Are you new to Git and GitHub or just want a detailed guide on getting started with version control? Check out our [Version Control chapter](https://the-turing-way.netlify.com/version_control/version_control.html) in _The Turing Way_ Book!

### 4. Submit a [pull request][github-pullrequest]

We encourage you to open a pull request as early in your contributing process as possible.
This allows everyone to see what is currently being worked on.
It also provides you, the contributor, feedback in real-time from both the community and the continuous integration as you make commits (which will help prevent stuff from breaking).

When you are ready to submit a pull request, you will automatically see the [Pull Request Template](https://github.com/chrisdburr/turing-commons/master/.github/ISSUE_TEMPLATE/ISSUE_TEMPLATE.md) contents in the pull request body.
It asks you to:

- Describe the problem you're trying to fix in the pull request, reference any related issue and use fixes/close to automatically close them, if pertinent.
- List of changes proposed in the pull request.
- Describe what the reviewer should concentrate their feedback on.

By filling out the "_Lorem ipsum_" sections of the pull request template with as much detail as possible, you will make it really easy for someone to review your contribution!

If you have opened the pull request early and know that its contents are not ready for review or to be merged, add "[WIP]" at the start of the pull request title, which stands for "Work in Progress".
When you are happy with it and are happy for it to be merged into the main repository, change the "[WIP]" in the title of the pull request to "[Ready for review]".

A member of _The Turing Commons_ team will then review your changes to confirm that they can be merged into the main repository.
A [review][github-review] will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation.

You can update your [fork][github-fork] of _The Turing Commons_ [repository][turing-commons-repo] and the pull request will automatically update with those changes.
You don't need to submit a new pull request when you make a change in response to a review.

You can also submit pull requests to other contributors' branches!
Do you see an [open pull request](https://github.com/chrisdburr/turing-commons/pulls) that you find interesting and want to contribute to?
Simply make your edits on their files and open a pull request to their branch!

GitHub has a [nice introduction][github-flow] to the pull request workflow, but please [get in touch](#get-in-touch) if you have any questions :balloon:.

<!-- ## Style Guide

In _The Turing Way_'s [Community Handbook](https://the-turing-way.netlify.app/community-handbook/community-handbook.html), we have developed a style guide for the project.

[_The Turing Way_ style guide](https://the-turing-way.netlify.app/community-handbook/style.html) will provide guidance and supporting resources for ensuring consistency, readability and accessibility for all our users.

You are welcome to contribute to the style guide by opening [a new issue](https://github.com/alan-turing-institute/the-turing-way/issues/new/choose). -->

## Recognising Contributions

We welcome and recognise all kinds of contributions, from fixing small errors, to developing documentation, maintaining the project infrastructure, writing chapters or reviewing existing resources.
_The Turing Commons_ follows the [all-contributors][all-contributors] specifications.
The all-contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).
You can see a list of current contributors [here](https://github.com/chrisdburr/turing-commons/blob/master/contributors.md). 😍

To add yourself or someone else as a contributor, comment on the relevant Issue or Pull Request with the following:

```
@all-contributors please add <username> for <contributions>
```

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types.
The bot will then create a Pull Request to add the contributor and reply with the pull request details.

**PLEASE NOTE: Only one contributor can be added with the bot at a time!**
Add each contributor in turn, merge the pull request and delete the branch (`all-contributors/add-<username>`) before adding another one.
Otherwise, you can end up with dreaded [merge conflicts][github-mergeconflicts].
Therefore, please check the open pull requests first to make sure there aren't any [open requests from the bot](https://github.com/chrisdburr/turing-commons/pulls/app%2Fallcontributors) before adding another.

What happens if you accidentally run the bot before the previous run was merged and you got those pesky merge conflicts?
(Don't feel bad, we have all done it! 🙈)
Simply close the pull request and delete the branch (`all-contributors/add-<username>`).

Finally, don't forget to add yourself to the list of contributors [here](https://github.com/chrisdburr/turing-commons/blob/master/contributors.md)!

---

_These Contributing Guidelines have been adapted from the [Contributing Guidelines](https://github.com/alan-turing-institute/the-turing-way/blob/master/CONTRIBUTING.md) of the [Turing Way](https://github.com/alan-turing-institute/the-turing-way)—a superb, community-led how-to guide for reproducible data science! (License: CC-BY)_

[git]: https://git-scm.com
[github]: https://github.com
[github-branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[github-fork]: https://help.github.com/articles/fork-a-repo
[github-flow]: https://guides.github.com/introduction/flow
[github-mergeconflicts]: https://help.github.com/articles/about-merge-conflicts
[github-pullrequest]: https://help.github.com/articles/creating-a-pull-request
[github-review]: https://help.github.com/articles/about-pull-request-reviews
[github-syncfork]: https://help.github.com/articles/syncing-a-fork
[markdown]: https://daringfireball.net/projects/markdown
[rick-roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[jerry-maguire]: https://media.giphy.com/media/uRb2p09vY8lEs/giphy.gif
[all-contributors]: https://github.com/kentcdodds/all-contributors#emoji-key
[turing-commons-repo]: https://github.com/chrisdburr/turing-commons
[turing-commons-issues]: (https://github.com/chrisdburr/turing-commons/issues)
