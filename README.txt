*******************
zope.deferredimport
*******************

Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used.  You
can also cause deprecation warnings to be issued when a variable is
used.

.. contents::

Releases
********

==================
1.0   (2007/02/18)
==================

Initial public release zope.deferredimport
