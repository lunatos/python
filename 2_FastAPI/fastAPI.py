from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    id: Optional[int] = None

users = {
    1: {"username": "teste1", "email": "teste1@email.com", "id": 1},
    2: {"username": "teste2", "email": "teste2@email.com", "id": 2},
    3: {"username": "teste3", "email": "teste3@email.com", "id": 3}
}

@app.get("/")
async def home():
    return users

@app.post("/create-user/", response_model=User)
def create_user(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    user.id = len(users) + 1 
    #para rodar asincronamente seria bom adicionar uma nova logica mais robusta
    users[user.id] = user
    return user

@app.get("/get-user/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]