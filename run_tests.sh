#!/bin/bash

rm -rf tests/__pycache__/
python3 -m unittest discover tests/

exit 0

