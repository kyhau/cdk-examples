# cdk-blank-python

This repo shows how to deploy [blank_python](https://github.com/awsdocs/aws-lambda-developer-guide/tree/master/sample-apps/blank-python) with CDK.

Project structure
- app.py
- build_layer.sh, build and package the Layer.
- [cdk_blank_python/](cdk_blank_python) contain the CDK app
- [function/](function)  contains the lambda function
- [layer/](layer)  contains what to be built and packaged for the Layer
- [tests/](tests)  contains test data and scrtpts to run unit tests and lambda test

Prerequisites
1. Install CDK v2: `npm install -g aws-cdk@next`
2. Update env_dev.json

Build and Deploy
```bash
pip install -r requirements.txt

cd tests
./run_unittests.sh
cd -

./build_layer.sh

cdk ls

cdk synth

cdk deploy

cd tests/
./test_lambda.sh
cd -
```
