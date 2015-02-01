``zope.deferredimport``
=======================

.. image:: https://pypip.in/version/zope.deferredimport/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/zope.deferredimport/
    :alt: Latest Version

.. image:: https://travis-ci.org/zopefoundation/zope.deferredimport.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.deferredimport

.. image:: https://readthedocs.org/projects/zopedeferredimport/badge/?version=latest
        :target: http://zopedeferredimport.readthedocs.org/en/latest/
        :alt: Documentation Status

Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used.  You
can also cause deprecation warnings to be issued when a variable is
used.

