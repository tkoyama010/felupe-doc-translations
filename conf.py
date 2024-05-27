# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized paraview-docs document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs`.
- Overrides source directory as 'felupe/docs`.

"""
import os
import pathlib

basedir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "felupe/docs"
)
exec(pathlib.Path(os.path.join(basedir, "conf.py")).read_text(), globals())
locale_dirs = [os.path.join(basedir, "../../locale/")]


def setup(app):
    app.srcdir = basedir
    app.confdir = app.srcdir
