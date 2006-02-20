##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os, re, shutil, sys, tempfile, unittest
from zope.testing import doctest, renormalizing
import zope.deferredimport

class OutErr:

    @staticmethod
    def write(message):
        sys.stdout.write(message)

def setUp(test):
    d = test.globs['tmp_d'] = tempfile.mkdtemp('deferredimport')
    shutil.copy(
        os.path.join(os.path.dirname(__file__), 'sample1.py.in'),
        os.path.join(d, 'sample1.py'),
        )
    shutil.copy(
        os.path.join(os.path.dirname(__file__), 'sample2.py.in'),
        os.path.join(d, 'sample2.py'),
        )
    zope.deferredimport.__path__.append(d)
    sys.modules.pop('zope.deferredimport.sample1', None)
    sys.modules.pop('zope.deferredimport.sample2', None)

    test.globs['oldstderr'] = sys.stderr
    sys.stderr = OutErr

def tearDown(test):
    sys.stderr = test.globs['oldstderr'] 

    zope.deferredimport.__path__.pop()
    shutil.rmtree(test.globs['tmp_d'])
    sys.modules.pop('zope.deferredimport.sample1', None)
    sys.modules.pop('zope.deferredimport.sample2', None)

def test_suite():
    checker = renormalizing.RENormalizing((
        (re.compile('.+/README.txt'), 'README.txt'),
        ))
    return doctest.DocFileSuite(
        'README.txt',
        setUp=setUp, tearDown=tearDown,
        optionflags=doctest.NORMALIZE_WHITESPACE,
        checker=checker,
        )

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

