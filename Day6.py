"""
Functional requirements

Create a task with:

title (string, required)

completed (boolean, default = False)

Each task must have an auto-generated id.

Get:

all tasks

a single task by id

Mark a task as completed using its id.

Validation & errors

If title is empty → return 400

If task id does not exist → return 404

Use proper HTTPException codes

API design

Use a class to store tasks (similar to your DB class)

Use Pydantic models for request bodies

No database (in-memory only)

Endpoints to implement

POST /tasks

GET /tasks

GET /tasks/{id}

PUT /tasks/{id}/complete

"""



from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

app = FastAPI()

class Input(BaseModel):
    task : str = Field(...)
    completed : bool = Field(default=False)

class ToDo:
    def __init__(self):
        self.todo_list = []
        self.next_id = 1 
    def add_field(self,task:str,completed:bool):

        field = {
            "id" : self.next_id,
            "task" : task,
            "completed" : completed
        }
        self.todo_list.append(field)
        self.next_id += 1
        return field
    
    def get_fields(self):
        return self.todo_list
    def get_field_id(self,task_id):
        for each in self.todo_list:
            if task_id == each["id"]:
                return each
        raise HTTPException(status_code=404,detail="id not found ")
    def mark_complete(self,task_id):
        for each in self.todo_list:
            if task_id == each["id"]:
                each["completed"] = True
                return each
        raise HTTPException(status_code=404,detail="id not found ")

    
ft = ToDo()

@app.post("/tasks")
def add_task(data:Input):
    if data.task.strip() == "":
        raise HTTPException(status_code=400,detail="task cannot be empty")
    return ft.add_field(data.task,data.completed)
@app.get("/tasks")
def get_task():
    return ft.get_fields()
@app.get("/tasks/{id}")
def get_task_id(id:int):
    return ft.get_field_id(id)
@app.put("/tasks/{id}/complete")
def mark_true(id:int):
    return ft.mark_complete(id)



    
    


