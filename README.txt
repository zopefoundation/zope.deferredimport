Deferred Import
===============

Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.

The zope.deferredimport.define function supports this.  You can use
the function to define one or more names to be imported when they are
accessed.  Simply provide names as keyword arguments with import
specifiers as values.  The import specifiers are given as atrings of
the form "module:name", where module is the dotted name of the 
module and name is a, possibly dotted, name of an object within the
module. 

To see how this works, see the sample modules, sample1 and sample2.
The sample1 module defines several values as deferred imports of and
from sample 2.  The sample2 module prints a message when it is
imported.  When we import sample1, we don't see a message until we
access a variable:

    >>> import zope.deferredimport.sample1
    >>> print zope.deferredimport.sample1.one
    Sampe 2 imported!
    1

    >>> import zope.deferredimport.sample2

    >>> zope.deferredimport.sample1.sample2 is zope.deferredimport.sample2
    True

Note that a deferred attribute appears in a module's dictionary *after* 
it is accessed the first time:

    >>> 'two' in zope.deferredimport.sample1.__dict__
    False

    >>> zope.deferredimport.sample1.two
    2

    >>> 'two' in zope.deferredimport.sample1.__dict__
    True

Deferred attributes can also be marked as deprecated, in which case, a
message will be printed the first time they are accessed:

    >>> zope.deferredimport.sample1.three is zope.deferredimport.sample2.C
    README.txt:1: 
    DeprecationWarning: three is deprecated. Will go away in 2007.
      Deferred Import
    True

Of course, non-deferred variables are accessible as usuall:

    >>> print zope.deferredimport.sample1.four
    4

    >>> print zope.deferredimport.sample1.five
    5
