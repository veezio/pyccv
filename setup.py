# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Setup file for CCV bindings."""

from setuptools import setup, find_packages

VERSION = (0, 1, '0dev')

setup(
    name='pyccv',
    version='.'.join([str(x) for x in VERSION]),
    description='Python ctypes bindings for the ccv library.',
    author='veezio',
    author_email='contact@veez.io',
    url='http://veez.io',
    py_modules=["ccv"]
)
