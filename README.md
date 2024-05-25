# FElupe official documentation translations

This is a project to provide FElupe official documentation, hosted on
the Read The Docs platform, in multiple languages.

.. note:: The current procedure is bit tricky because Read The Docs
doesn't have a way to specify options for `sphinx-build` command.
**conf.py** files for each languages have `language` and `locale_dirs`
values without having full copy of **conf.py** of FElupe doc. If we want
to specify **conf.py** file that is out of source directory, we will use
`-c` option for the `sphinx-build` command. Unfortunately Read the Docs
doesn't support that. If there is a better way, open an issue.

## How the translated documentation projects are setup on RTD

Instructions:
https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Key points:

-   There is a RTD project for each language.
-   Each project needs the correct **Language** setting on the
    **Settings** page.
-   The parent project needs connections created to each translated
    project on the **Translations Settings** page.

.. list-table:: :header-rows: 1

-   -   Build Status
    -   felupe-doc docs
    -   RTD Project

-   -   .. image::
        https://readthedocs.org/projects/felupe/badge/?version=latest
        :target: https://www.felupe-doc.org/en/main/?badge=main :alt:
        Documentation Status
    -   http://www.felupe-doc.org/en
    -   https://readthedocs.org/projects/felupe/ (Parent project)

-   -   .. image::
        https://readthedocs.org/projects/felupe-ja/badge/?version=latest
        :target: https://www.felupe-doc.org/ja/main/?badge=main :alt:
        Documentation Status
    -   http://www.felupe-doc.org/ja
    -   https://readthedocs.org/projects/felupe-ja/

## How to add a new language translation

1.  Add new language to `locale/update.sh`:

    .. code-block:: diff

    -   rm -R es ja
    -   tx pull -l es,ja
    -   rm -R es ja pt_BR
    -   tx pull -l es,ja,pt_BR

2.  Update po files:

    .. code-block::

    sh ./locale/update.sh

3.  Commit them

4.  Add new project on Read The Docs. For example, for `pt_BR`:

    https://readthedocs.org/projects/felupe-pt-br/

    .. note:: If a RTD project name for a translation is already taken,
    create a unique project name instead. For example, when `felupe-ru`
    was taken, `felupe-doc-ru` was used instead.

5.  Add new translation project to parent project:

    https://readthedocs.org/dashboard/felupe/translations/