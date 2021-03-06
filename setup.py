#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='pygeda',
    version='0.1',
    description='EDA and PCB support for GEDA',
    author='Markus Hutzler',
    author_email='markus.hutzler@me.com',
    classifiers=[
        "Development Status :: 2 - Pre Alpha",
        "Intended Audience :: Developers",
        "License :: GPL License",
        "Topic :: Electronic Design :: Tools",
        "Programming Language ::Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(),
    license='GPL3',
    package_dir={'pygeda': 'pygeda'},
    entry_points={
        "console_scripts": [
            "pygeda=pygeda.main:main",
        ],
    }
)
