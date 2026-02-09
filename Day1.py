"""
Write a POST /predict API that:

Accepts JSON input with fields x and y (both integers)

Returns their sum as JSON

Validates that both values are required and integers 

"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    x: int
    y: int = 0

@app.post("/predict")
def predict(data : Input):
    result = data.x + data.y
    return {"sum": result}