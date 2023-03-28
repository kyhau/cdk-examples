from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class LayerDateTimeNowStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        test_lambda : _lambda.Function = LayerDateTimeNowStack.create_lambda(self)

    @staticmethod
    def create_lambda(self) -> None:
        lambda_function: _lambda.Function = _lambda.Function(
            self, "test_lambda",
            function_name="TestLambdaLayerDateTimeNow",
            handler="TestLambdaLayerDateTimeNow.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("function"),
        )

        layer = _lambda.LayerVersion(
            self, "l1",
            code=_lambda.AssetCode("layer"),
            description="DateTimeNow cdk-lambda-layer-datetimenow",
            layer_version_name="DateTimeNow"
        )

        lambda_function.add_layers(layer)

        return lambda_function
