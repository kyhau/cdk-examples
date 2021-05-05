from aws_cdk import Stack
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class CdkBlankPythonStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        function_name = "BlankPythonCdkDemo"
        custom_role: _iam.Role = CdkBlankPythonStack.create_role(self, f"{function_name}Role")
        test_lambda: _lambda.Function = CdkBlankPythonStack.create_lambda(self, function_name, custom_role)

    @staticmethod
    def create_role(self, role_name: str) -> None:
        lambda_role: _iam.Role = _iam.Role(
            self, "test_lambda_role",
            assumed_by=_iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaReadOnlyAccess"),
                _iam.ManagedPolicy.from_aws_managed_policy_name("AWSXrayWriteOnlyAccess"),
            ],
            role_name=role_name,
        )
        return lambda_role

    @staticmethod
    def create_lambda(self, function_name: str, custom_role: _iam.Role) -> None:
        lambda_function: _lambda.Function = _lambda.Function(
            self, "test_lambda",
            code=_lambda.Code.from_asset("function", exclude=["*.test.py"]),
            function_name=function_name,
            handler="lambda_function.lambda_handler",
            role=custom_role,
            runtime=_lambda.Runtime.PYTHON_3_8,
        )

        layer = _lambda.LayerVersion(
            self, "layer_1",
            code=_lambda.AssetCode("package"),
            description="aws-xray-sdk for tracing",
            layer_version_name="aws-xray-sdk"
        )

        lambda_function.add_layers(layer)

        return lambda_function
