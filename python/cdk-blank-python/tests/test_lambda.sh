#!/bin/bash
set -eo pipefail

while true; do
  aws lambda invoke --function-name BlankPythonCdkDemo \
    --cli-binary-format raw-in-base64-out \
    --payload file://event.json out.json
  cat out.json
  echo ""
  sleep 2
done
