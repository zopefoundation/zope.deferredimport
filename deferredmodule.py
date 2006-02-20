##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Modules with defered attributes

$Id$
"""

import sys
import warnings

class Module(object):

    def __init__(self, old):
        self.__dict__ = old.__dict__
        self.__original_module__ = old

    def __repr__(self):
        return `self.__original_module__`

class Deferred(object):

    def __init__(self, name, specifier):
        self.__name__ = name
        self.specifier = specifier

    _import_chicken = {}, {}, ['*']

    def __get__(self, inst, class_):
        if inst is None:
            return self

        specifier = self.specifier
        if ':' in specifier:
            module, name = specifier.split(':')
        else:
            module, name = specifier, ''

        v = __import__(module, *self._import_chicken)
        if name:
            for n in name.split('.'):
                v = getattr(v, n)
        setattr(inst, self.__name__, v)
        return v

class DeferredAndDeprecated(Deferred):

    def __init__(self, name, specifier, message):
        self.__name__ = name
        self.specifier = specifier
        self.message = message
        

    def __get__(self, inst, class_):
        if inst is None:
            return self

        warnings.warn(
            self.__name__ + " is deprecated. " + self.message,
            DeprecationWarning, stacklevel=2)
        return Deferred.__get__(self, inst, class_)


def getClass():
    __name__ = sys._getframe(2).f_globals['__name__']
    module = sys.modules[__name__]
    cls = module.__class__
    if not issubclass(cls, Module):
        cls = type(__name__ + 'Class', (Module, ), {})
        module = cls(module)
        sys.modules[__name__] = module
    return cls

def define(**names):
    cls = getClass()
    for name, specifier in names.iteritems():
        setattr(cls, name, Deferred(name, specifier))

def deprecated(message, **names):
    cls = getClass()
    for name, specifier in names.iteritems():
        setattr(cls, name, DeferredAndDeprecated(name, specifier, message))
    
