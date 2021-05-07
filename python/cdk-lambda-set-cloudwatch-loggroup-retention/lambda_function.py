import json
import logging
import os

import boto3

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("botocore").setLevel(logging.CRITICAL)
logging.getLogger("boto3").setLevel(logging.CRITICAL)
logging.getLogger("urllib3.connectionpool").setLevel(logging.CRITICAL)
logging.info(f"boto3.__version__: {boto3.__version__}")

client = boto3.client("logs")

LOGGROUP_PREFIX = os.environ.get("LOGGROUP_PREFIX")
RETENTION_DAYS = os.environ.get("RETENTION_DAYS", 1)


def lambda_handler(event, context):
    params = {} if LOGGROUP_PREFIX is None else {"logGroupNamePrefix": LOGGROUP_PREFIX}

    dry_run = event.get("dry_run", False)

    ret = {}

    for page in client.get_paginator("describe_log_groups").paginate(**params).result_key_iters():
        for item in page:
            loggroup_name = item["logGroupName"]
            retention = item.get("retentionInDays")
            logging.info(f"{loggroup_name}, {retention}")

            if dry_run:
                ret[loggroup_name] = "" if retention is None else str(retention)

            elif RETENTION_DAYS != retention:
                logging.info(f"Updating {loggroup_name} to {RETENTION_DAYS}")

                resp = client.put_retention_policy(
                    logGroupName=loggroup_name,
                    retentionInDays=RETENTION_DAYS,
                )
                logging.info(resp)

    result = {"message": "succeeded"}
    if ret:
        result["results"] = ret

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
