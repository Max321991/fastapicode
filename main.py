from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city:str
    pincode:int
class User(BaseModel):
    name:str
    age:int
    address:Address

@app.get("/")
def home():
    return {"message": "Hello you are under venv"}

@app.get("/about")
def about():
    return {"message": "This is about page by fastApi"}

@app.get("/users")
def user():
    return {
        "users" : ['Mohit', 'Rohit', 'Suresh']
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user_id": user_id}

@app.get("/max")
def get_max(name: str = None):
    return { "name" : name}

@app.get("/items")
def get_items(name: str = None, price: int = 0):
    return {
        "name" : name,
        "price" : price
    }

@app.post("/create-user")
def create_user(user:User):
    return{
        "message": "User Create",
        "data" : user
    }

@app.post("/create-client")
def create_client(user:User):
    return{
        "message" : "Create Client",
        "data" : user
    }