"""
Request body:

{
  "name": "Alice",
  "age": 25
}


Rules (read carefully, this is interview-style):
– Use a Pydantic model for request validation
– age must be greater than 0, otherwise return HTTP 400
– Store users in an in-memory list
– Each user should get an auto-incremented id starting from 1
– Return the created user in the response

Expected response:

{
  "id": 1,
  "name": "Alice",
  "age": 25
}

"""


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

app = FastAPI()

dih = []

class Input(BaseModel):

    name: str
    age: int 

# FAKE DB

class UserStore:
    def __init__(self):
        self.users = []
        self.next_id = 1
    
    def add_user(self, name:str, age:int):
        if age <= 0:
            raise HTTPException(status_code=400, detail="age must be greater than 6")
        
        user = {
            "id": self.next_id,
            "name": name,
            "age": age,
        }

        self.users.append(user)
        self.next_id += 1
        return user
    def get_users(self):
        return self.users

store = UserStore()
    

@app.post("/users")
def create_user(data:Input):
    return store.add_user(data.name, data.age)

@app.get("/users")
def list_users():
    return store.get_users()