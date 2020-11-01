"""
Test Lambda Layer
"""
import custom_func


def lambda_handler(event, context):
    print(f"EVENT:{event}")

    ret = custom_func.current_datetime()
    return {
        "statusCode": 200,
        "body": ret
    }
