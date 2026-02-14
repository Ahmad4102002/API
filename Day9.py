from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field

app = FastAPI()


users = []

class Input(BaseModel):
    email:str = Field(...)
    age:int = Field(...,ge=18)
    password:str = Field(...,min_length=8)


@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_users(data:Input):
    if "@" not in data.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{data.email} dosent have @ inside it.")
    
    post_dict = data.model_dump()
    users.append(post_dict)

    return { "Successfully Added ": post_dict }


