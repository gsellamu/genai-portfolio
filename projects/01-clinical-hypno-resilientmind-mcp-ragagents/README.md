# Clinical Hypnotherapy ResilientMind Agentic Platform (Prototype)
**Role:** Architect/Developer · **Stack:** Python, FastAPI, OpenAI, Docker, GCP/AWS

**Problem:** Functional health signals (hydration, stress, movement) swing labs/symptoms.  
**Solution:** GenAI + XR/VR + IoT biofeedback loops that coach hydration/movement/relaxation.

## Highlights
- **Design:** Event-driven pipeline; guardrails; privacy-by-default
- **Models:** LLM coach; embeddings for recall; eval harness
- **Data:** Pseudonymized device + lab samples; lineage noted
- **Ops:** Docker local; IaC WIP; CI placeholders

## How to Run (Windows PowerShell)
```powershell
# create & activate venv
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# install deps
pip install -r requirements.txt

# run API
uvicorn src.app.main:app --reload

## Demos
- Chat transcript(s): `./chats/`
- Diagrams: `./docs/` (see `system-context.md`, `architecture.png`)


