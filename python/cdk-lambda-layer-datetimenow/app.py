#!/usr/bin/env python3
import json
import os
from aws_cdk.core import App, Environment
from cdk_layer_datetimenow.lambda_layer import LayerDateTimeNowStack


env_file = os.environ.get("ENV_FILE", "env_dev.json")
with open(env_file) as json_file:
    stage_env = json.load(json_file)


app = App()

LayerDateTimeNowStack(app, "cdk-lambda-layer-datetimenow", env=Environment(**stage_env))

app.synth()