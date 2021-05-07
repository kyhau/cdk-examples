from aws_cdk import Duration, Stack, aws_iam, aws_lambda
from constructs import Construct

lambda_dir = "function"


class CdkBlankPythonStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        function_name = "BlankPythonCdkDemo"
        custom_role: aws_iam.Role = CdkBlankPythonStack.create_role(self, function_name)
        test_lambda: aws_lambda.Function = CdkBlankPythonStack.create_lambda(self, function_name, custom_role)

    @staticmethod
    def create_role(self, function_name: str) -> None:
        role_name = f"{function_name}-ExecutionRole"

        lambda_role: aws_iam.Role = aws_iam.Role(
            self, role_name,
            assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            inline_policies = {
                f"{function_name}-ExecutionPolicy": aws_iam.PolicyDocument(
                    statements=[
                        aws_iam.PolicyStatement(
                            actions=[
                                "lambda:GetAccountSettings",
                            ],
                            effect=aws_iam.Effect.ALLOW,
                            resources=["*"],
                        )
                    ]
                )
            },
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSXrayWriteOnlyAccess"),
            ],
            role_name=role_name,
        )
        return lambda_role

    @staticmethod
    def create_lambda(self, function_name: str, custom_role: aws_iam.Role) -> None:
        lambda_function: aws_lambda.Function = aws_lambda.Function(
            self, function_name,
            code=aws_lambda.Code.from_asset(
                lambda_dir,
                exclude=["*.test.py"]
            ),
            function_name=function_name,
            handler="lambda_function.lambda_handler",
            role=custom_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            timeout= Duration.seconds(300),
        )

        layer = aws_lambda.LayerVersion(
            self, "AWSXraySdkLayer",
            code=aws_lambda.AssetCode("package"),
            description="aws-xray-sdk for tracing",
            layer_version_name="aws-xray-sdk"
        )

        lambda_function.add_layers(layer)

        return lambda_function
