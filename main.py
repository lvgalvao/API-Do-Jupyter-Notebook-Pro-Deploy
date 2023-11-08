from fastapi import FastAPI
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

app = FastAPI()


class ModeloProduto(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    preco: float


produtos: List[ModeloProduto] = [
    {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preco": 5.00,
    },
    {
        "id": 2,
        "titulo": "Workshop",
        "descricao": "Workshop de deploy",
        "preco": 100.00,
    },
    {
        "id": 3,
        "titulo": "Iphone",
        "descricao": "Iphone 14",
        "preco": 2000,
    },
]


@app.get("/")
def ola_mundo():
    """
    View raiz, retorna {"Hello": "World"}
    """
    return {"Hello": "World"}


@app.get("/produtos", response_model=List[ModeloProduto])
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos
