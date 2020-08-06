#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Install the <your_project_name> package and its requirements."""

# 3rd party libraries
from setuptools import setup

# If you adjust any of the following, run `pip-compile` to update the requirements.txt
# You can find `pip-compile` in https://github.com/jazzband/pip-tools
install_requires = [
]
tests_require = [
    "pytest",
    "pytest-mccabe",
    "pytest-flake8",
    "pytest-black",
    "pytest-pydocstyle",
]  # noqa

setup(
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},
)
