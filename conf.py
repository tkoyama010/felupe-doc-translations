# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized felupe-docs document.

For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs`.
- Overrides source directory as 'felupe/docs`.

"""

from pathlib import Path

basedir = Path(__file__).resolve().parent / "felupe/docs/src"
exec((basedir / "conf.py").read_text(), globals())  # noqa: S102
locale_dirs = [basedir / "../../../locale/"]


def setup(app) -> None:  # noqa: D103,ANN001
    app.srcdir = basedir
    app.confdir = app.srcdir
