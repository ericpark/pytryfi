#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from pytryfi.const import PYTRYFI_VERSION

if sys.argv[-1] == 'compile':
    os.system('python setup.py bdist_wheel')
    sys.exit()

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

pkg = find_packages("pytryfi")
print(pkg)

setup(
    name="pytryfi", # Replace with your own username
    version=PYTRYFI_VERSION,
    author="Eric Park",
    author_email="eric@ericspark.com",
    description="Python Interface for TryFi Dog Collars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericpark/pytryfi",
    packages={'pytryfi', 'pytryfi/common'},
    include_package_data=True,
    classifiers=[ "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: Apache Software License",
                    "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'sentry-sdk',
    ],
    python_requires='>=3.6',
)
# Instructions

# source env/bin/activate
# pip install wheel build
# python3 setup.py sdist