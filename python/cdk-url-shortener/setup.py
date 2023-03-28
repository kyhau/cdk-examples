import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="url_shortener",
    version="0.1.0",

    description="A CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "url_shortener"},
    packages=setuptools.find_packages(where="url_shortener"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-apigateway",
        "aws-cdk.aws-dynamodb",
        "aws-cdk.aws-ecs",
        "aws-cdk.aws-ec2",
        "aws-cdk.aws-lambda",
        "cdk-watchful",
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
