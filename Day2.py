from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
import os 


app = FastAPI()

API_KEY = os.getenv("API_KEY","dev-key")

class Input(BaseModel):
    x: int
    y: int

def verify_api_key(x_api_key:str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401,detail="Invalid or Missing API Key")

@app.post("/predict",dependencies=[Depends(verify_api_key)])
def predict(data:Input):
    result = data.x + data.y
    if result > 100:
        raise HTTPException(status_code=400, detail ="sum too large" )
    return {"sum" : result}
    
@app.get("/health")
def health():
    return {"status": "OK"}