# Python project template files
Template files for bootstrapping a new Python project.

## Purpose
Bootstrapping a new Python project requires some steps to take and files to create. This project is a set of basic configuration and environments files that are usually needed by every Python project. Default Python version for this project chosen - 3.8.

## Directory structure
The project consists of <project_name> (replace with your project name), and tests folder.  Separating these two folders allows deploying files only from <project_name> folder, leaving the test folder only for testing purposes. 

## Tools used in this project
We use the following tools for purposes of testing, styling, and type checking. Many of them find their configuration in project root's setup.cfg.

- pytest
  - Widely used package for testing and style-checking in Python
  - Install: pip install pytest
  - Run: pytest . from project root
- flake8
  - Checks code style against PEP8 and tons of other stuff (e.g. blank lines, unused imports, max line length, cyclomatic complexity, ...)
  - Install: pip install pytest-flake8
  - Run: pytest . --flake8 from project root
- black
  - Automatic code formatter
  - Install: pip install black
  - Run: black . from project root
- pydocstyle
  - Checks style of docstrings
  - Install: pip install pytest-pydocstyle
  - Run: pytest . --pydocstyle from project root
- tox
  - Ad-hoc virtual environment to test code with fresh Python runtime, helps with testing if setup.py includes everything it needs to
  - Install: pip install tox
  - Run: tox from project root
- mypy
  - (Very non-perfect) type checking for Python
  - Install: pip install mypy
  - Run: mypy . --ignore-missing-imports from project root

## How to bootstrap a new Python project
Copy contents of the project directory, then:
1. Rename README.md.template file to README.md so that you have a template readme file. Edit this file accordingly.
2. Change folder name "project_name" according to your project name
3. Update setup.cfg and setup.py files, replace <your_project_name> with your project name, and edit corresponding fields according to your needs.

