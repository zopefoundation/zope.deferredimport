Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used.  You
can also cause deprecation warnings to be issued when a variable is
used.

.. contents::

Changes
=======

3.5.0 (unreleased)
------------------

- Added support to bootstrap on Jython.


3.4.0 (2007/07/19)
------------------

- Finished release of zope.deferredimport.


3.4.0b1 (2007/07/09)
--------------------

- Initial release as a separate project, corresponds to zope.deferredimport
  from Zope 3.4.0b1.
