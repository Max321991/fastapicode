from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name :str
    age: int
    password: str

class UserResponse(BaseModel):
    name:str
    age: int

@app.get("/response_user", response_model=UserResponse)
def get_user():
    return {
        "name": "Mohit",
        "age": 23,
        "password": "abc123"
    }
