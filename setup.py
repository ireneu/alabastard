#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('alabaster/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='alabastard',
    version=version,
    description='Son of alabaster: A configurable sidebar-enabled Sphinx theme',
    long_description=readme,
    author='Ireneu Pla',
    author_email='ireneup@gmail.com',
    packages=['alabastard'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
