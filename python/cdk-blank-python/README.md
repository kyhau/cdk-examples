# cdk-blank-python

This repo shows how to deploy [blank_python](https://github.com/awsdocs/aws-lambda-developer-guide/tree/master/sample-apps/blank-python) with CDK.

Project structure
- app.py
- build_layer.sh, build and package the Layer.
- [cdk_blank_python/](cdk_blank_python) contain the CDK app
- [function/](function)  contains the lambda function
- [layer/](layer)  contains what to be built and packaged for the Layer
- [tests/](tests)  contains test data and scrtpts to run unit tests and lambda test


Steps
```bash
pip install -r requirements.txt

pushd tests
./run_unittests.sh
popd

./build_layer.sh

cdk ls

cdk synth

cdk deploy

pushd tests/
./test_lambda.sh
popd
```
