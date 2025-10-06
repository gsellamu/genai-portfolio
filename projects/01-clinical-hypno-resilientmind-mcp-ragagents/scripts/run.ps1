# run.ps1 - start API with venv
if (-not (Test-Path .\.venv)) { python -m venv .venv }
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt 2>$null
uvicorn --app-dir src app.main:app --reload
