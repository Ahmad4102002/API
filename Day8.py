"""
Design an API for user registration.

You must create:
POST /users to register a user with email, password, and age.

Rules you must enforce:
Email must contain @.
Password length must be at least 8.
Age must be ≥ 18.

If validation fails, return proper HTTP status codes.
Store users in memory using a class (like your ToDo example).
Do NOT return the password in responses.

What I'll check: request body validation, clean error handling, and response safety.
"""


from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field

app = FastAPI()


class Input(BaseModel):
    email : str 
    password : str = Field(...,min_length=8)
    age : int = Field(...,ge=18)

## FAKE IN MEMORY DB 

class Fake:
    def __init__(self):
        self.users = []
    def add_user(self,email,password,age):
        user = {
            "email": email,
            "password": password,
            "age": age
        }

        self.users.append(user)

    def find_user(self):
        return [
            {
                "email": user["email"],
                "age": user["age"]
            }
            for user in self.users
        ]
fake = Fake()

@app.post("/users",status_code=status.HTTP_201_CREATED)
def add_users(data:Input):
    if "@" not in data.email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"@ not found in {data.email}")
    fake.add_user(data.email,data.password,data.age)
    return {"detail" : "Added Successfully" }

@app.get("/users")
def get_users():
    return fake.find_user()



