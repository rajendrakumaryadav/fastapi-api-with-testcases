from typing import Annotated

from fastapi import FastAPI, Form
from .db import curd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}


@app.post("/register")
async def register(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    """
    Register a new user
    :param username: str - username
    :param password: str - password
    :return: User object - new user details

    This function accepts username and password as form
    data and creates a new user in the database.
    """
    user_curd = curd.UserCRUD()
    user = curd.User(username=username, password=password)
    new_user: curd.User = user_curd.create_user(user)
    return new_user


@app.put("/update-password")
async def update_password(username: Annotated[str, Form()], password: Annotated[str, Form()],
                          new_password: Annotated[str, Form()]):
    # TODO: Update user password in database
    return {"message": "Password updated successfully"}


@app.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    user = curd.UserCRUD()
    user.delete_user(user_id)
    return {"message": "User deleted successfully"}


@app.get("/users")
async def get_users():
    user = curd.UserCRUD()
    users = user.get_users()
    return users
