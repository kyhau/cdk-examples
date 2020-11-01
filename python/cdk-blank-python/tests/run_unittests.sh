#!/bin/bash
set -eo pipefail

# Create and activate virtual env

pip install -r requirements-test.txt

python3 ../function/lambda_function.test.py
