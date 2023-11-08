from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_response():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}


def test_products_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200


def test_products_list():
    response = client.get("/produtos")
    assert response.json() == [
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
            "preco": None,
        },
    ]
