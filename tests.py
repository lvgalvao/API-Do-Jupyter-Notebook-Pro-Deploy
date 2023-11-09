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


def test_inserir_produto():
    # Dados do produto que vamos inserir
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição do Produto Teste",
        "preco": 19.99,
    }

    # Simula uma requisição POST para a rota /produtos
    response = client.post("/produtos", json=produto_data)

    # Verifica se o status code da resposta é 200 (OK)
    assert response.status_code == 200

    # Verifica se a resposta segue o modelo ModeloItem
    response_data = response.json()
    assert response_data["titulo"] == produto_data["titulo"]
    assert response_data["descricao"] == produto_data["descricao"]
    assert response_data["preco"] == produto_data["preco"]
