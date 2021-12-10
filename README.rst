=========================
 ``zope.deferredimport``
=========================

.. image:: https://img.shields.io/pypi/v/zope.deferredimport.svg
        :target: https://pypi.python.org/pypi/zope.deferredimport/
        :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/zope.deferredimport.svg
        :target: https://pypi.org/project/zope.deferredimport/
        :alt: Supported Python versions

.. image:: https://github.com/zopefoundation/zope.deferredimport/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/zope.deferredimport/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.deferredimport/badge.svg?branch=master
        :target: https://coveralls.io/github/zopefoundation/zope.deferredimport?branch=master

.. image:: https://readthedocs.org/projects/zopedeferredimport/badge/?version=latest
        :target: http://zopedeferredimport.readthedocs.io/en/latest/
        :alt: Documentation Status

Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used.  You
can also cause deprecation warnings to be issued when a variable is
used.

Documentation is hosted at https://zopedeferredimport.readthedocs.io/
