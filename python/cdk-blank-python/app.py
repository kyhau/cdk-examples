#!/usr/bin/env python3
import json
import os
from aws_cdk.core import App, Environment
from cdk_blank_python.lambda_layer_xray_sdk import CdkBlankPythonStack


env_file = os.environ.get("ENV_FILE", "env_dev.json")
with open(env_file) as json_file:
    stage_env = json.load(json_file)


app = App()

CdkBlankPythonStack(app, "cdk-blank-python", env=Environment(**stage_env))

app.synth()
