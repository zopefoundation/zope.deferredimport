zope.deferredimport Package Readme
==================================

Overview
--------

Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used.  You
can also cause deprecation warnings to be issued when a variable is
used, but we'll get to that later.

The zope.deferredimport.define function can be used to define one or
more names to be imported when they are accessed.  Simply provide
names as keyword arguments with import specifiers as values.  The
import specifiers are given as strings of the form "module:name",
where module is the dotted name of the module and name is a, possibly
dotted, name of an object within the module.
