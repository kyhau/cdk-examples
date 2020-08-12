#!/bin/bash
set -e

# TODO Create a virtualenv for the project

pip install -r requirements.txt

cat > env_dev.json << EOF
{
  "account": "1234567890",
  "region": "ap-southeast-2"
}
EOF

cdk ls

cdk synth
