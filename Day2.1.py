"""
Requirements

Create a FastAPI app

Add a POST /v1/predict endpoint

The endpoint must:

Accept JSON body with:

x (required integer, ≥ 0)

y (optional integer, default 0, ≥ 0)

Return { "sum": <x + y> }

If x + y > 100, return HTTP 400 with message "sum too large"

Protect /v1/predict using an API key:

Header name: X-API-Key

Value read from env var API_KEY

Fallback value: "dev-key"

Missing or wrong key → 401 Unauthorized

Add a public GET /health endpoint that returns { "status": "OK" }

The API must be runnable using:

"""

from fastapi import FastAPI,HTTPException, Header, Depends
from pydantic import BaseModel,Field
import os 
app = FastAPI()

API_KEY = os.getenv("API_KEY","dev-key")

class Input(BaseModel):
    x : int = Field(...,ge=0)
    y : int = Field(0,ge=0)

def verify_api_key(x_api_key: str|None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401,detail="Invalid or Missing API key")

@app.post("/v1/predict",dependencies=[Depends(verify_api_key)])
def predict(data:Input):
    result = data.x + data.y
    if result > 100:
        raise HTTPException(status_code=400,detail="Sum too large")
    return {"sum" : result }

@app.get("/health")
def health():
    return {"Status" : "OK"}

