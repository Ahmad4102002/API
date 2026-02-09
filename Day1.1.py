"""
Next question (ready when you are):
Add input validation so that x must be ≥ 0 and y must be ≥ 0.

"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Input(BaseModel):
    x:int = Field(..., ge=0)
    y:int = Field(0, ge=0)

@app.post("/predict")
def predict(data: Input):
    result = data.x + data.y
    return {"sum" : result}