# O que é uma API?

Uma API (Application Programming Interface) é um conjunto de rotinas e padrões (contratos) estabelecidos por uma aplicação, para que outras aplicações possam utilizar as funcionalidades dessa aplicação.

![Imagem](assets/server-server.png)

# Por que usar uma API?

Nos últimos anos, a Internet se transformou de uma rede de servidores web que serviam principalmente páginas estáticas para navegadores de internet...

![Internet](https://thefloppydisk.files.wordpress.com/2013/05/web10.png?w=1248)

...em uma arquitetura cliente-servidor, onde aplicativos web e mobile se comunicam com diferentes aplicações, cada vez mais por meio de APIs RESTful simples, mas poderosas.

![Imagem](https://thefloppydisk.files.wordpress.com/2013/05/web20.png?w=1245)

# As regras do jogo

Basicamente uma API é um contrato que define como uma aplicação vai se comunicar com a outra. Como os dados serão enviados e recebidos.

![Contrato](assets/contract.png)

# O que é uma API REST?

REST é um acrônimo para REpresentational STATE Transfer, que é um estilo de arquitetura para sistemas distribuídos.

![Rest](assets/apirest.png)

# Que ferramentas podemos usar em Python?

Temos muitas opções....

![Rest](assets/framework.png)

...mas vamos de FastAPI!

Para saber mais sobre alternativas, inspiração e comparações [veja aqui](https://fastapi.tiangolo.com/)

# Como se comunicar com ela?

- Nosso protocolo (ex: http)

- Nosso servidor tem um endereço (ex: rickandmortyapi.com)

- Nosso servidor tem uma porta (ex: 8080 para http e 443 para https)

- E precisamos acessar um recurso ou como constumamos chamar, endpoint ou rota (ex: /api/character)

``` 
https://rickandmortyapi.com:443/api/character
```

# Nossos verbos

O protocolo HTTP é a base usada por trás das APIs REST e as "requisita" utilizando diversos "tipos". Os mais comuns são:

O que é o CRUD? 

Create, Read, Update e Delete

- POST: (Create) Criar um recurso
- GET: (Read) Obter um recurso
- PUT: (Update) Atualizar um recurso
- DELETE: Remover um recurso

# Qual a diferença entre REST e RESTful?

REST é um estilo de arquitetura para sistemas distribuídos, enquanto RESTful é a implementação desse estilo.

# Vamos para a prática?

Vamos usar o VScode e o terminal para criar nossa primeira API.

# Criando nosso ambiente virtual
Ambientes virtuais são uma ferramenta para manter as dependências necessárias para diferentes projetos em locais separados, evitando problemas de compatibilidade.

```bash
python -m venv .venv
```

# Ativando nosso ambiente virtual

```bash
source .venv/bin/activate
```

# Instalando o FastAPI
O FastAPI é um framework para criação de APIs RESTful com Python.


```
pip install fastapi
```

# Instalando o Uvicorn
O Uvicorn é um servidor ASGI de alto desempenho, construído com base no Starlette e o servidor padrão recomendado para o FastAPI. ASGI é uma especificação para servidores Python que permite que eles sejam compatíveis com frameworks assíncronos, como o FastAPI. Assíncrono significa que o servidor pode lidar com mais de uma solicitação ao mesmo tempo.

```
pip install uvicorn
```

# Criando nosso primeiro endpoint
Endpoints são os pontos de acesso de uma API. Eles são definidos por uma URL, um método e um conjunto de parâmetros.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

# Executando o servidor
Para executar o servidor, precisamos usar o Uvicorn e passar o nome do arquivo e o nome da variável que contém a instância do FastAPI.

```
uvicorn main:app --reload
```

# Criando nosso primeiro teste
Testes automatizados são uma parte importante do desenvolvimento de software. Eles são usados para garantir que o código que escrevemos faça o que esperamos que ele faça.

```bash
touch tests.py
```

```bash
pip install pytest
```

```python
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_response():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}
```

# Rodando os testes

```bash
pytest -v tests.py
```

# Colocando nosso CI para funcionar
CI (Continuous Integration) é uma prática de desenvolvimento de software onde os desenvolvedores integram seu código em um repositório compartilhado com frequência, onde testes e builds são executados automaticamente.

```bash
touch .github/workflows/main.yml
```

```yaml
name: CI

on: pull_request

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v3

      - name: Set up python
        id: setup-python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install requirements
        run: pip install -r requirements.txt

      - name: List directory contents
        run: ls -la

      - name: Run tests
        run: pytest -v tests.py
```

# Criando nossa segunda view
Modificando o arquivo main.py

```python

produtos: List[Dict[str, Any]] = [
    {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preço": 5.0,
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
        "preço": None,
    },
]

@app.get("/produtos")
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos
```

# Adicionando o tipo de retorno Pydantic

```
pip install pydantic
```

```python
from Pydantic import BaseModel

class Produto(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    preco: float

@app.get("/produtos", response_model=List[ModeloProduto])

```

# Pydantic já trabalhando

```bash

  {'type': 'missing', 'loc': ('response', 0, 'preco'), 'msg': 'Field required', 'input': {'id': 1, 'titulo': 'Cadeira Gamer', 'descricao': 'Cadeira confortável para fazer live', 'preço': 5.0}, 'url': 'https://errors.pydantic.dev/2.4/v/missing'}
  {'type': 'missing', 'loc': ('response', 1, 'titulo'), 'msg': 'Field required', 'input': {'id': 2, 'a titulo': 'Workshop', 'descricao': 'Workshop de deploy', 'preço': 100.0}, 'url': 'https://errors.pydantic.dev/2.4/v/missing'}
  {'type': 'missing', 'loc': ('response', 1, 'preco'), 'msg': 'Field required', 'input': {'id': 2, 'a titulo': 'Workshop', 'descricao': 'Workshop de deploy', 'preço': 100.0}, 'url': 'https://errors.pydantic.dev/2.4/v/missing'}
  {'type': 'missing', 'loc': ('response', 2, 'titulo'), 'msg': 'Field required', 'input': {'id': 3, 'a titulo': 'Iphone', 'descricao': 'Iphone 14', 'preço': 2000.0}, 'url': 'https://errors.pydantic.dev/2.4/v/missing'}
  {'type': 'missing', 'loc': ('response', 2, 'preco'), 'msg': 'Field required', 'input': {'id': 3, 'a titulo': 'Iphone', 'descricao': 'Iphone 14', 'preço': 2000.0}, 'url': 'https://errors.pydantic.dev/2.4/v/missing'}

  ```

Refatorando, criar uma branch chamada data

Vamos criar um arquivo data.py

Jogar a nossa lista para lá

Refatorando, criar uma branch chamada modelos.py

```python

from typing import Optional
from pydantic import BaseModel, PositiveFloat


class ModeloItem(BaseModel):
    """
    Modelo para um item de produto
    """

    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat

```

Vamos criar também 4 novos testes

```python
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
```

# Colocando nossa aplicação no Ar

Vamos usar o site

https://dashboard.render.com/login

![Render](assets/render1.png)

![Render2](assets/render2.png)

![Render3](assets/render3.png)

Configuração do Uvicorn

uvicorn main:app --host 0.0.0.0 --port 10000

# Vamos criar nossa rota post

https://kinsta.com/pt/blog/lista-codigos-status-http/#:~:text=200%20C%C3%B3digos%20de%20status&text=200%3A%20%E2%80%9CEst%C3%A1%20tudo%20bem.,resultado%2C%20criou%20um%20novo%20recurso.

Mudar o código para 201

na main.py adicionar

```python
@app.post("/produtos", response_model=ModeloItem)
def inserir_produto(item_a_inserir: ModeloItem):
    """
    View que adiciona um novo produto
    """
    return produtos.inserir(item_a_inserir.model_dump())
```

no data.py adicionar
```python
    def inserir(self, item: Dict[str, any]) -> Dict[str, any]:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.produtos = self.produtos.append(item)
        return item
```

no tests.py adicionar
```
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
```

# Verificar se nossa CI/CD está funcionando

push post

PR post to main

Avaliar!

