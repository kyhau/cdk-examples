# CDK Lambda Layer DateTimeNow Demo

This is a simple example to show how to deploy Lambda Layer with CDK.

Project structure
- app.py
- [cdk_layer_datetimenow/](cdk_layer_datetimenow) contains the CDK app
- [function/](function) contains the lambda function
- [layer/](layer) contains what to be built and packaged for the Layer
- test_lambda.sh tests the lambda function after deployment

Steps
```bash
pip install -r requirements.txt
cdk ls
cdk synth
cdk deploy
./test_lambda.sh
```

References:
1. https://stackoverflow.com/questions/59716366/how-to-deploy-and-attach-a-layer-to-aws-lambda-function-using-aws-cdk-and-python
1. https://stackoverflow.com/questions/55695187/import-libraries-in-lambda-layers
    > According to the video they should go in either /opt/python or /opt/python/lib/python3.6/site-packages. The video also gives the indication that if you're using 3.7 or above you have to use the second one but I tried it in just /opt/python with 3.8 and it seemed to work. I feel like for simplicity it would be easier to just put in /opt/python but if you're making a layer for multiple versions then maybe you would want to do the second.

