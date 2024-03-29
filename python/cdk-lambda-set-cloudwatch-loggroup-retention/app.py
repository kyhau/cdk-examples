#!/usr/bin/env python3
import json
import os
from os.path import abspath, dirname

from aws_cdk import (App, Duration, Environment, Stack, aws_events,
                     aws_events_targets, aws_iam, aws_lambda)
from constructs import Construct

lambda_dir = dirname(abspath(__file__))


class CdkSetCwLoggroupRetentionStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        function_name = "SetCwLoggroupRetention"
        custom_role = CdkSetCwLoggroupRetentionStack.create_role(self, function_name)
        main_function = CdkSetCwLoggroupRetentionStack.create_lambda(self, function_name, custom_role)
        event_rule = CdkSetCwLoggroupRetentionStack.create_event_rule(self, main_function)

    @staticmethod
    def create_role(self, function_name: str) -> None:
        lambda_role: aws_iam.Role = aws_iam.Role(
            self, f"{function_name}-ExecutionRole",
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            description=f"{function_name}-ExecutionRole",
            inline_policies = {
                f"{function_name}-ExecutionPolicy": aws_iam.PolicyDocument(
                    statements=[
                        aws_iam.PolicyStatement(
                            actions=[
                                "logs:DescribeLogGroups",
                                "logs:PutRetentionPolicy",
                            ],
                            effect=aws_iam.Effect.ALLOW,
                            resources=["*"],
                        )
                    ]
                )
            },
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
            ],
            role_name=f"{function_name}-ExecutionRole",
        )
        return lambda_role

    @staticmethod
    def create_lambda(self, function_name: str, custom_role: aws_iam.Role) -> None:
        lambda_function: aws_lambda.Function = aws_lambda.Function(
            self, function_name,
            code=aws_lambda.Code.from_asset(
                lambda_dir,
                exclude=[
                    "cdk.out",
                    "tests",
                    "app.py",
                    "*.test.py",
                    "*.json",
                    "*.md",
                    "*.txt",
                ]
            ),
            function_name=function_name,
            handler="lambda_function.lambda_handler",
            role=custom_role,
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            timeout= Duration.seconds(300),
        )
        return lambda_function

    @staticmethod
    def create_event_rule(self, main_function: aws_lambda.Function) -> None:
        rule: aws_events.Rule = aws_events.Rule(
            self, "EventRule",
            schedule=aws_events.Schedule.expression("cron(0 1 ? * SUN *)"),
        )
        rule.add_target(aws_events_targets.LambdaFunction(main_function))


env_file = os.environ.get("ENV_FILE", "env_dev.json")
with open(env_file) as json_file:
    stage_env = json.load(json_file)

app = App()

CdkSetCwLoggroupRetentionStack(app, "cdk-set-cw-loggroup-retention", env=Environment(**stage_env))

app.synth()
