import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="cdk_layer_datetimenow",
    version="0.1.0",

    description="A CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="kyhau",

    package_dir={"": "cdk_layer_datetimenow"},
    packages=setuptools.find_packages(where="cdk_layer_datetimenow"),

    install_requires=[
        "aws-cdk-lib>=2.0.0rc1",
        "constructs>=10.0.0",
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 1 - Beta",
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
