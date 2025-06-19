#!/bin/bash
cd /home/kavia/workspace/code-generation/eventmaster-api-112527-d6c135b4/eventmaster_api
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

