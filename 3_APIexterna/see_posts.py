import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        return [Post(**post) for post in response.json()]
    else:
        raise HTTPException(status_code=404, detail='Posts not found')

app = FastAPI()

@app.get("/")
async def home():
    return get_posts()

#Se a minha api forsse protegida por token, ao usuário requisitar os posts
#ele deveria enviar o token na requisição para minha API e o get_posts()
#iria ser executada no servidor apenas se o token enviado pelo usuário fosse válido

#Se a api pública fosse protegida por token, eu iria deixar esse token protejido no servidor
#e toda vez que ele fosse fazer a requisição no servidor ele iria enviar esse toquen junto