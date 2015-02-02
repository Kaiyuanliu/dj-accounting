#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import dj_accounting
version = dj_accounting.__version__

setup(
    name='dj-accounting',
    version=version,
    author='',
    author_email='jungle.chuan@gmail.com',
    packages=[
        'dj_accounting',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['dj_accounting/manage.py'],
)
