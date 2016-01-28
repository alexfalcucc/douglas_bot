#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'schedule',
    'telepot',
    'pickledb',
    'pyvirtualdisplay',
    'webdriverplus',
    'eatiht',
    ]

setup(name='douglas_bot',
      version='0.0',
      description='telegram bot',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        ],
      author='',
      author_email='',
      url='',
      keywords='bot telegram script python',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
