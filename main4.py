from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse


app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request, exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found"
        }
    )


@app.get("/user/{name}")
def get_user(name:str):
    if name != "mohit":
        raise UserNotFoundException(name)
    return{
        "name":name
    }

# @app.post("/create_user", status_code= status.HTTP_201_CREATED)
# def create_user():
#     return {
#         "message":"User Created"
#     }

# @app.get("/user")
# def get_users():
#     return{
#         "status":"Success",
#         "message":"User Fetched",
#         "data":{
#             "name": "Mohit",
#             "age":24
#         }
#     }

# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not Found"
#         )
#     return {
#         "id": 1,
#         "name": "Mohit"
#     }