# test.ps1 - run pytest with venv
if (-not (Test-Path .\.venv)) { python -m venv .venv }
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt 2>$null
pytest -q
