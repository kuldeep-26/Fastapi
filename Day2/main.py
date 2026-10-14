from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post('/create_user')
def create_user(user:User):
    return {
        "message":"User created successfully",
        "user":user
    }



# Todo app:----

todos = []

class Todo(BaseModel):
    id:int
    task:str
    completed:bool

@app.post('/todo')
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"Todo added",
        "data":todo
    }

@app.get('/todo_list')
def todo_list():
    return {
        'data':todos
    }

@app.get('/get_todo/{todo_id}')
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message":"id not found"}

@app.put('/update_todo/{todo_id}')
def update_todo(todo_id:int, updated_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "message":"data updated",
                "data":update_todo
            }
    return {"error":"todo not found"}

@app.delete("todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message":"Data Deleted"}
    return {"error":"todo not found"}



# todos = [
#         {
#             "id":1,
#             'name':"harsh"
#             'class':"secondary"
#         },
#         {
#             "id":2,
#             'name':"many"
#         },
#         {
#             "id":3,
#             'name':"many"
#         },
#     ]