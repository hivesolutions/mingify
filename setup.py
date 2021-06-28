#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name = "mingify",
    version = "0.1.2",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Mingify",
    license = "Apache License, Version 2.0",
    keywords = "mingify url minification",
    url = "http://www.hive.pt",
    zip_safe = False,
    packages = [
        "mingify",
        "mingify.controllers",
        "mingify.controllers.api",
        "mingify.controllers.web",
        "mingify.models"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    install_requires = [
        "appier",
        "appier_extras",
        "jinja2",
        "pymongo"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
