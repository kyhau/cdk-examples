# CDK Examples

[![githubactions](https://github.com/kyhau/cdk-examples/workflows/Build-Test/badge.svg)](https://github.com/kyhau/cdk-examples/actions)
[![travisci](https://travis-ci.org/kyhau/cdk-examples.svg?branch=master)](https://travis-ci.org/kyhau/cdk-examples)

This repository contains some AWS CDK projects implemented for demo.

- See [kyhau/cdk-examples/CDK/](https://github.com/kyhau/cdk-examples/tree/master/CDK) for some helper scripts to install CDK and set up dev environment.
- See [kyhau/cdk-examples/#cdk](https://github.com/kyhau/cdk-examples/#cdk) for some useful CDK resources.
- See also [Translating TypeScript AWS CDK code to other languages](https://docs.aws.amazon.com/cdk/latest/guide/multiple_languages.html) (JavaScript, Python, Java, C#).

---

## Examples in Python

| Example | Description |
| :--- | :--- |
| [cdk-blank-python](python/cdk-blank-python) | Deploy [blank_python](https://github.com/awsdocs/aws-lambda-developer-guide/tree/master/sample-apps/blank-python) (aws-xray-sdk with a Lambda layer and a dummy Lambda function using the layer) with CDK with unit tests |
| [cdk-lambda-layer-datetimenow](python/cdk-lambda-layer-datetimenow) | Deploy a Lambda layer and a dummy Lambda function using the layer, with invoke-lambda test |
| [cdk-lambda-set-cloudwatch-loggroup-retention/](cdk-lambda-set-cloudwatch-loggroup-retention/) | Deploy a Lambda functin and event rule to set CW loggroups retention |
| [cdk-url-shortener](python/cdk-url-shortener) | Deploy the URL Shortener illustrated in the [AWS Online Tech Talk - Infrastructure is Code with the AWS CDK](https://www.youtube.com/watch?v=ZWCvNFUN-sU) |
| [kyhau/have-a-smile](https://github.com/kyhau/have-a-smile) | Deploy a Lambda function that calls APIs of DevOps Reactions, Dilbert and xkcd |
