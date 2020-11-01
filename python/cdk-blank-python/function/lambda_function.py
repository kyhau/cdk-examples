import logging
import os

import boto3
import jsonpickle
from aws_xray_sdk.core import patch_all, xray_recorder

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

region = os.environ.get("AWS_REGION", "ap-southeast-2")

client = boto3.client("lambda", region_name=region)
client.get_account_settings()

def lambda_handler(event, context):
    logger.info("## ENVIRONMENT VARIABLES\r" + jsonpickle.encode(dict(**os.environ)))
    logger.info("## EVENT\r" + jsonpickle.encode(event))
    logger.info("## CONTEXT\r" + jsonpickle.encode(context))
    response = client.get_account_settings()
    return response["AccountUsage"]
