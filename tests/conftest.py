# conftest.py
import sys
import os
from fastapi.testclient import TestClient
import pytest

# Adiciona o diretório do projeto ao sys.path para resolver problemas de importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import app  # Importa o aplicativo FastAPI


@pytest.fixture(scope="module")
def test_client():
    """
    Cria uma instância de TestClient que pode ser usada em testes.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def produto_id(test_client):
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição Teste",
        "preco": 19.99,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 201
    return response.json()["id"]
