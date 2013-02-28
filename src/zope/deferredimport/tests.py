##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
"""Tests
"""
import doctest
import os
import re
import shutil
import sys
import tempfile
import warnings

from zope.testing import renormalizing
import zope.deferredimport


class OutErr:

    @staticmethod
    def write(message):
        sys.stdout.write(message)


def warn(message, type_, stacklevel):
    frame = sys._getframe(stacklevel)
    path = frame.f_globals['__file__']
    file = open(path)
    lineno = frame.f_lineno
    for i in range(lineno):
        line = file.readline()
    file.close()

    print("%s:%s: %s: %s\n  %s" % (
        path,
        frame.f_lineno,
        type_.__name__,
        message,
        line.strip(),
        ))


def setUp(test):
    # Py3: The old method of creating a tempdir and adding it to the
    # module.__path__ does not work reliably in Python 3.3.
    d = test.globs['tmp_d'] = os.path.join(os.path.dirname(__file__), 'samples')

    def create_module(**modules):
        for name, src in modules.items():
            fn = os.path.join(d, name+'.py')
            needs_update = True
            if os.path.exists(fn):
                with open(fn, 'r') as file:
                    needs_update = file.read() != src
            if needs_update:
                with open(fn, 'w') as file:
                    file.write(src)
            test.globs['created_modules'].append(name)

    test.globs['created_modules'] = []
    test.globs['create_module'] = create_module

    import zope.deferredimport
    zope.deferredimport.__path__.append(d)

    test.globs['oldstderr'] = sys.stderr
    sys.stderr = OutErr

    test.globs['saved_warn'] = warnings.warn
    warnings.warn = warn

def tearDown(test):
    sys.stderr = test.globs['oldstderr']

    zope.deferredimport.__path__.pop()
    for name in test.globs['created_modules']:
        sys.modules.pop(name, None)
    warnings.warn = test.globs['saved_warn']


def test_suite():
    checker = renormalizing.RENormalizing((
        (re.compile(r'.+[/\\]README.txt'), 'README.txt'),
        ))
    return doctest.DocFileSuite(
        'README.txt',
        setUp=setUp, tearDown=tearDown,
        optionflags=doctest.NORMALIZE_WHITESPACE,
        checker=checker,
        globs = {'__file__': os.path.join(
                    os.path.dirname(__file__), 'README.txt')}
        )
