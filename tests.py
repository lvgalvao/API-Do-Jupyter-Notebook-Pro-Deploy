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
