from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/")
async def read_users():
    return [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
    ]

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}

@app.post("/users/")
async def create_user(user: User):
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}