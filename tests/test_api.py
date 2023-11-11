import pytest
from fastapi.testclient import TestClient
from app.main import app

from pydantic import ValidationError


@pytest.fixture
def test_client():
    """
    Cria uma instância de TestClient que pode ser usada em testes.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def produto_id(test_client):
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição Teste",
        "preco": 19.99,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 201
    return response.json()["id"]


def test_listar_produtos(test_client):
    response = test_client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se a resposta é uma lista


def test_inserir_produto(test_client):
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição Teste",
        "preco": 19.99,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == produto_data["titulo"]
    assert data["descricao"] == produto_data["descricao"]
    assert data["preco"] == produto_data["preco"]
    # Armazena o ID do produto criado para uso em testes futuros


def test_obter_produto(test_client, produto_id):
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == produto_id
    assert "titulo" in data


def test_atualizar_produto(test_client, produto_id):
    novo_dado = {
        "titulo": "Produto Atualizado",
        "descricao": "Descrição Atualizada",
        "preco": 29.99,
    }
    response = test_client.put(f"/produtos/{produto_id}", json=novo_dado)
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == novo_dado["titulo"]


def test_remover_produto(test_client, produto_id):
    response = test_client.delete(f"/produtos/{produto_id}")
    assert response.status_code == 200
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 404


from app.schemas import ProdutoSchema


def test_modelo_produto_valido():
    produto = ProdutoSchema(titulo="Teste", descricao="Descrição Teste", preco=10.0)
    assert produto.titulo == "Teste"
    assert produto.preco == 10.0


def test_modelo_produto_invalido():
    with pytest.raises(ValidationError):
        ProdutoSchema(titulo="", preco=-10.0)
