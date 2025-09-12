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
# This package is developed by the Zope Toolkit project, documented here:
# https://zopetoolkit.readthedocs.io/
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.deferredimport package
"""
import os

from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


TESTS_REQUIRE = [
    'zope.testrunner >= 6.4',
]

DOCS_REQUIRE = [
    'Sphinx',
    'repoze.sphinx.autointerface',
]

setup(
    name='zope.deferredimport',
    version='6.0',
    url='http://github.com/zopefoundation/zope.deferredimport',
    license='ZPL-2.1',
    description=('zope.deferredimport allows you to perform imports names '
                 'that will only be resolved when used in the code.'),
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'zope.deferredimport/issues'),
        'Sources': 'https://github.com/zopefoundation/zope.deferredimport',
    },

    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
    ),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'zope.proxy',
    ],
    extras_require={
        'test': TESTS_REQUIRE,
        'docs': DOCS_REQUIRE,
    },
    include_package_data=True,
    zip_safe=False,
)
