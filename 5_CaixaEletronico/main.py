from fastapi import FastAPI, Body
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

class Req(BaseModel):
    valor: int

def calcula_saque(value: int) -> dict:
    if value <= 0:
        raise HTTPException(status_code=400, detail="Valor invalido, tente sacar um valor positivo")

    notas = [100, 50, 20, 10, 5, 2]
    saque = {}

    for nota in notas:
        saque[str(nota)] = value // nota
        value %= nota

    if value > 0:
        raise HTTPException(status_code=400, detail="Não é possivel sacar este valor no caixa")

    return saque

@app.post("/api/saque")
async def saque(req: Req):
    return calcula_saque(req.valor)