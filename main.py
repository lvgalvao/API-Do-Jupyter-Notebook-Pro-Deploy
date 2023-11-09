from fastapi import FastAPI
from typing import List
from data import Produtos
from modelos import ModeloItem

app = FastAPI()
produtos = Produtos()


@app.get("/")
def ola_mundo():
    """
    View raiz, retorna {"Hello": "World"}
    """
    return {"Hello": "World"}


@app.get("/produtos", response_model=List[ModeloItem])
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos.listar()
