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


@app.post("/produtos", response_model=ModeloItem)
def inserir_produto(item_a_inserir: ModeloItem):
    """
    View que adiciona um novo produto
    """
    # o item_a_inserir é do tipo ModeloItem, que é um Pydantic Model
    # Precisamos passar ele para dict para que o método inserir
    return produtos.inserir(item_a_inserir.model_dump())
