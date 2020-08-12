#!/usr/bin/env python3
import json
import os
from aws_cdk.core import App
from url_shortener.url_shortener_stack import (
    UrlShortenerStack,
    TrafficStack,
)

"""
ENV_FILE should be set to a json file containing:
{
  "account": "todo",
  "region": "todo",
}
"""
env_file = os.environ.get("ENV_FILE", "env_dev.json")

with open(env_file) as json_file:
    stage_env = json.load(json_file)


app = App()

UrlShortenerStack(app, "url-shortener", env=stage_env)

#TrafficStack(app, "url-shortener-load-test", env=stage_env)

app.synth()
