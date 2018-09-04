#!/bin/bash

echo "Packager"

SPECDIR="./build/specs"
PYINSOPTION="--clean -F --specpath $SPECDIR"

echo "Packaging with $PYINSOPTION"

pyinstaller --version
pytest -v -ra

if [ $? -eq 1 ]
then
    echo "Test failed. See above for details"
fi

pyinstaller $PYINSOPTION calculator.py
pyinstaller $PYINSOPTION palindromechecker.py
pyinstaller $PYINSOPTION sendemail.py
pyinstaller $PYINSOPTION getdate.py

echo "End of script."
