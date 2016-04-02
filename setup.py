#!/usr/bin/env python

#
# Copyright (c) 2013, Digium, Inc.
# Copyright (c) 2016, fokin.denis@gmail.com
#

"""Setup script
"""

import os

from setuptools import setup

setup(
    name="aioswaggerpy",
    version="0.0.1",
    license="BSD 3-Clause License",
    description="Asynchronous library for accessing Swagger-enabled API's",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.rst")).read(),
    author="Denis Fokin",
    author_email="fokin.denis@gmail.com",
    url="https://github.com/dfokin/aioswagger-py",
    packages=["aioswaggerpy"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=["nose", "tissue", "coverage", "httpretty"],
    install_requires=["requests", "websocket-client"],
    entry_points="""
    [console_scripts]
    swagger-codegen = aioswaggerpy.codegen:main
    """
)
