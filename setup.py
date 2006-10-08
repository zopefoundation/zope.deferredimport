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
"""Setup for zope.deferredimport package

$Id$
"""

import os

try:
    from setuptools import setup, Extension
except ImportError, e:
    from distutils.core import setup, Extension

setup(name='zope.deferredimport',
      version='3.3-dev',
      url='http://svn.zope.org/zope.deferredimport',
      license='ZPL 2.1',
      description='Zope Deferredimport',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="The zope.deferredimport.define function can be used to"
                       "define one or more names to be imported when they are"
                       "accessed.  Simply provide names as keyword arguments"
                       "with import specifiers as values.  The import"
                       "specifiers are given as strings of the form"
                       "'module:name', where module is the dotted name of"
                       "the module and name is a, possibly dotted, name of"
                       "an object within the module.",

      packages=['zope', 'zope.deferredimport'],
      package_dir = {'': 'src'},

      namespace_packages=['zope',],
      tests_require = ['zope.testing'],
      install_requires=['zope.interface',
                        'zope.proxy'],
      include_package_data = True,

      zip_safe = False,
      )
