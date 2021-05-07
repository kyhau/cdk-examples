# cdk-lambda-set-cloudwatch-loggroup-retention

Lambda and event rule to set CW loggroups retention (deployment with CDK)

Prerequisites
1. Install CDK v2: `npm install -g aws-cdk@next`
2. Update env_dev.json

Build and Deploy
```bash
pip install -r requirements.txt

cdk ls

cdk synth

cdk deploy

cd tests/
./test_lambda.sh
cd -
```