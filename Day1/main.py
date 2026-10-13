from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to fastapi"}

@app.get('/user/{user_id}')
def get_user(user_id:int):
    return {"user_id": user_id}

@app.get('/product')
def product(name:str=None, price:int=100):
    return {
        "name":name,
        "price":price
    }

class User(BaseModel):
    name: str
    age: int

@app.post('/create_user')
def user(user:User):
    return{
        "message":"user created successfully",
        "user":user
    }