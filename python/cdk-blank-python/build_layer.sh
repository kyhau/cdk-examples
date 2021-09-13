#!/bin/bash
set -eo pipefail

rm -rf package

cd layer
pip install --target ../package/python -r requirements.txt
