#!/usr/bin/python3

import os
import re
from setuptools import setup, find_packages


def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as f:
        return f.read()

def _get_version_match(content):
    # Search for lines of the form: # __version__ = 'ver'
    regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_match = re.search(regex, content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def get_version(path):
    return _get_version_match(read_file(path))

NAME = 'rmsdk'

requirements = [
    'pycryptodome',
    'requests'
]

setup(
    name=NAME,
    version=get_version(os.path.join(NAME, '__init__.py')),
    description='A Python wrapper around the Revenue Monster API',
    long_description=read_file('README.rst'),
    keywords='RevenueMonster SDK API',
    author='Rex Low',
    author_email='rex@revenuemonster.my',
    maintainer='Rex Low',
    url='https://github.com/RevenueMonster/RM-API-SDK-Python',
    license='MIT',
    install_requires=requirements,
    packages=[NAME],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)