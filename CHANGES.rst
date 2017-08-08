=========
 Changes
=========

4.2.0 (2017-08-08)
==================

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6 and 3.3.

- Convert doctests to Sphinx documentation, including building docs
  and running doctest snippets under ``tox``.


4.1.0 (2014-12-26)
==================

- Add support for PyPy.  PyPy3 support is blocked on release of fix for:
  https://bitbucket.org/pypy/pypy/issue/1946

- Add support for Python 3.4.

- Add support for testing on Travis.


4.0.0 (2013-02-28)
==================

- Add support for Python 3.3.

- Drop support for Python 2.4 and 2.5.


3.5.3 (2010-09-25)
==================

- Add test extra to declare test dependency on ``zope.testing``.


3.5.2 (2010-05-24)
==================

- Fix unit tests broken under Python 2.4 by the switch to the standard
  library ``doctest`` module.


3.5.1 (2010-04-30)
==================

- Prefer the standard library's ``doctest`` module to the one from
  ``zope.testing``.


3.5.0 (2009-02-04)
==================

- Add support to bootstrap on Jython.

- Add reference documentation.


3.4.0 (2007-07-19)
==================

- Finish release of ``zope.deferredimport``.


3.4.0b1 (2007-07-09)
====================

- Initial release as a separate project, corresponding to the
  ``zope.deferredimport`` from Zope 3.4.0b1.
