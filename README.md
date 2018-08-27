# Scripts
Scripts written in python.

[![Build Status](https://travis-ci.org/ferdinh/python-scripts.svg?branch=master)](https://travis-ci.org/ferdinh/python-scripts)

### Scripts Available:
* Get Local and UTC Date
* SMTP E-mail Sending
* Text File Palindrome Checker
* Simple Calculator (Addition, Subtraction, Multiplication, Division)

# Requirements
This project requires a minimum version of python 3.6.

## Dependencies
* pytest

You can install all the dependencies by running `pip install -r requirements.txt`.

# Testing

This project uses __pytest__ as the testing framework.

To run the tests, you need to install pytest module into your machine using the command `pip install -U pytest` or refer to "Dependecies" section.
To install the module into specific version such as python 3.6, you can use `python3.6 -m pip install pytest` or suffix the targeted version.

After installing, you can check the version installed using `pytest --version`.

To run the test, simply type in `pytest` into the commandline. To test against specific python version, suffix the version number into  `python`. E.g To test against python 3.6 `python3.6 -m pytest`.
