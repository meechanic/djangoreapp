#!/usr/bin/env python

import os
from distutils.core import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='djangoreapp',
  version='0.0.1',
  packages=find_packages(),
  include_package_data=True,
  description='Django reusable app template package',
  long_description=README,
  author='Anybody Anybody',
  author_email='anybody@example.com',
  url='https://www.example.com/',
  license="MIT",
  classifiers=[
    'Framework :: Django',
    'Framework :: Django :: 1.10',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',  # example license
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
  ],
  packages=['djangoreapp']
)
