# FElupe official documentation translations

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

This is a project to provide FElupe official documentation, hosted on
the Read The Docs platform, in multiple languages.

> [!NOTE]
> The current procedure is bit tricky because Read The Docs
> doesn't have a way to specify options for `sphinx-build` command.
> **conf.py** files for each languages have `language` and `locale_dirs`
> values without having full copy of **conf.py** of FElupe doc. If we want
> to specify **conf.py** file that is out of source directory, we will use
> `-c` option for the `sphinx-build` command. Unfortunately Read the Docs
> doesn't support that. If there is a better way, open an issue.

## How the translated documentation projects are setup on RTD

Instructions:
https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Key points:

- There is a RTD project for each language.
- Each project needs the correct **Language** setting on the
  **Settings** page.
- The parent project needs connections created to each translated
  project on the **Translations Settings** page.

| Build Status                                                                                                                                          |                                               RTD Project |
| :---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------: |
| [![Documentation Status](https://readthedocs.org/projects/felupe/badge/?version=latest)](https://felupe.readthedocs.io/en/latest/?badge=latest)       | https://readthedocs.org/projects/felupe/ (Parent project) |
| [![Documentation Status](https://readthedocs.org/projects/felupe-ja/badge/?version=latest)](https://felupe-ja.readthedocs.io/ja/latest/?badge=latest) |               https://readthedocs.org/projects/felupe-ja/ |

## How to add a new language translation

1.  Add new language to `locale/update.sh`:

```diff
-   rm -R es ja
-   tx pull -l es,ja
+   rm -R es ja pt_BR
+   tx pull -l es,ja,pt_BR
```

2.  Update po files:

```
sh ./locale/update.sh
```

3.  Commit them

4.  Add new project on Read The Docs. For example, for `pt_BR`:

    https://readthedocs.org/projects/felupe-pt-br/

> [!NOTE]
> If a RTD project name for a translation is already taken,
> create a unique project name instead. For example, when `felupe-ru`
> was taken, `felupe-doc-ru` was used instead.

5.  Add new translation project to parent project:

    https://readthedocs.org/dashboard/felupe/translations/

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tkoyama010"><img src="https://avatars.githubusercontent.com/u/7513610?v=4?s=100" width="100px;" alt="Tetsuo Koyama"/><br /><sub><b>Tetsuo Koyama</b></sub></a><br /><a href="#translation-tkoyama010" title="Translation">🌍</a> <a href="#infra-tkoyama010" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/tkoyama010/felupe-doc-translations/commits?author=tkoyama010" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
