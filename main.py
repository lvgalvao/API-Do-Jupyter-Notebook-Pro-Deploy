from fastapi import FastAPI
from typing import List, Dict, Any


app = FastAPI()

produtos: List[Dict[str, Any]] = [
    {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preço": 1200.00,
    },
    {
        "id": 2,
        "a titulo": "Workshop",
        "descricao": "Workshop de deploy",
        "preço": 100.00,
    },
    {
        "id": 3,
        "a titulo": "Iphone",
        "descricao": "Iphone 14",
        "preço": 2000.00,
    },
]


@app.get("/")
def ola_mundo():
    """
    View raiz, retorna {"Hello": "World"}
    """
    return {"Hello": "World"}


@app.get("/produtos")
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos
