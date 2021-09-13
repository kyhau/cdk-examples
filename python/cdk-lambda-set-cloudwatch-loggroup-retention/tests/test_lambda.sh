#!/bin/bash
set -eo pipefail

aws lambda invoke --function-name SetCwLoggroupRetention \
  --cli-binary-format raw-in-base64-out \
  --payload file://event.json out.json
cat out.json
