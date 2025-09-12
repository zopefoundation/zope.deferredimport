=========
 Changes
=========

6.0 (2025-09-12)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


5.1 (2025-08-11)
================

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


5.0 (2023-06-29)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.11.


4.4 (2021-12-10)
================

- Add support for Python 3.8, 3.9 and 3.10.

- Drop support for Python 3.4.


4.3.1 (2019-08-05)
==================

- Avoid race condition in ``deferredmodule.ModuleProxy.__getattr__``
  `#8 <https://github.com/zopefoundation/zope.deferredimport/issues/8>`_.


4.3 (2018-10-05)
================

- Add support for Python 3.7.


4.2.1 (2017-10-24)
==================

- Preserve the docstrings of proxied modules created with
  ``deprecatedFrom``, ``deferredFrom``, etc. See `issue 5
  <https://github.com/zopefoundation/zope.deferredimport/issues/5>`_.


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
