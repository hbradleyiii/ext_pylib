#!/usr/bin/env python
# -*- coding: utf-8 -*-


from codecs import open
from setuptools import setup
from os import path

try:
   import pyandoc
   long_description = pyandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()


here = path.abspath(path.dirname(__file__))

setup(
    name = 'ext_pylib',

    version = '0.1',

    description = 'Extra python libraries for scaffolding server scripts.',
    long_description = long_description,

    # The project's main homepage.
    url = 'https://github.com/hbradleyiii/ext_pylib',

    # Author details
    author = 'Harold Bradley III',
    author_email = 'harold@bradleystudio.net',

    # Choose your license
    license = 'GPL v2',

    # See https://pypi.python.org/pypi?%3Aaction = list_classifiers
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords = 'server development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages = [
        'ext_pylib',
        'ext_pylib.domain',
        'ext_pylib.files',
        'ext_pylib.meta',
        'ext_pylib.password',
        'ext_pylib.prompt',
        'ext_pylib.user',
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires = ['pyandoc', 'requests'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require = {
        'test': ['pytest'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data = { },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files = [ ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points = { },
)
