from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Clinical Hypno  ResilientMind MCP RAG Agents")

class HydrationLog(BaseModel):
    timestamp: datetime
    ml: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/log/hydration")
def log_hydration(entry: HydrationLog):
    # placeholder: persist later
    print(f" Hydration Object = {entry.model_dump()}; {entry.model_dump_json()}")
    return {"accepted": True, "ml": entry.ml, "at": entry.timestamp.isoformat()}
