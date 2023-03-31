#!/usr/bin/env pwsh
python -m venv venv
. venv/bin/Activate.ps1
python -m pip install -r requirements.txt
$env:EXPLAIN_TEMPLATE_LOADING = $true
$env:FLASK_DEBUG = $true
