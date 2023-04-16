#!/usr/bin/env bash
# This script is supposed to be sourced from projects root folder
# For testing purposes only!
deactivate
. venv/bin/activate
python3 src/app.py testsecretkey
