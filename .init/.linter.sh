#!/bin/bash
cd /home/kavia/workspace/code-generation/ai-test-automation-platform-7982-7991/backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

