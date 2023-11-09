from fastapi.testclient import TestClient
import pytest
from pydantic import ValidationError

from modelos import ModeloItem

from main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_response():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}


def test_listar_response_json():
    response = client.get("/produtos")
    assert len(response.json()) == 3


# Teste para criar um item válido
def test_criar_modelo_item_valido():
    item = ModeloItem(
        titulo="Item Teste", descricao="Uma descrição qualquer", preco=10.99
    )
    assert item.titulo == "Item Teste"
    assert item.descricao == "Uma descrição qualquer"
    assert item.preco == 10.99


# Teste para falhar na criação de um item sem título
def test_criar_modelo_item_sem_titulo():
    with pytest.raises(ValidationError):
        item = ModeloItem(preco=10.99)


# Teste para falhar na criação de um item com preço negativo
def test_criar_modelo_item_com_preco_negativo():
    with pytest.raises(ValidationError):
        item = ModeloItem(titulo="Item Teste", preco=-10.99)


# Teste para falhar na criação de um item com preço igual a zero
def test_criar_modelo_item_com_preco_zero():
    with pytest.raises(ValidationError):
        item = ModeloItem(titulo="Item Teste", preco=0)
