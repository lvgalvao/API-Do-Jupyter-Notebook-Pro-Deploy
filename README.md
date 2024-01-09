# O que é uma API?

Uma API (Application Programming  Interface) é um conjunto de rotinas e padrões (contratos) estabelecidos por uma aplicação, para que outras aplicações possam utilizar as funcionalidades dessa aplicação.

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
poetry init
```

# Ativando nosso ambiente virtual

```bash
portey shell
```

```bash
poetry add taskipy
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

id_atual = 3

def lista(self):
    return self.produtos

def inserir(self, item: Dict[str, any]) -> Dict[str, any]:
    self.id_atual += 1
    item["id"] = self.id_atual
    return self.produtos.append(item)

@app.get("/produtos")
def listar_produtos():
    """
    View que que retorna o dicionário de produtos
    """
    return produtos
```

# Adicionando o tipo de retorno Pydantic

```bash
pip install pydantic
```

```python
from Pydantic import BaseModel

class Produto(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    preco: float

@app.get("/produtos", response_model=List[ModeloProduto], status_code=200)
def listar_produtos(item_a_inserir: ModeloProduto):
    """
    View que que retorna o dicionário de produtos
    """
    return produtos.inserir(item_a_inserir).dict()
```

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
from enum import Enum


class ProdutoSchema(BaseModel):
    """
    Modelo para um item de produto
    """

    id: Optional[int] = None
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    categoria: Categoria

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
```python
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

### Pequena refatoração

Vamos aproveitar para refatorar nosso projeto criando as pastas de APP e a pasta de testes

- Pontos importantes: data.py , main.py e modelos.py vão para app
- testes.py vai para testes e muda o nome para test_api.py
- Alterar no CI o nome do arquivo de testes
- Mover requirements.txt para a pasta APP
- Modificar o site RENDER para apontar para a pasta APP

### Conectar ao Banco de Dados

Adicionando as bibliotecas

```bash
poetry add sqlalchemy psycopg2-binary
```

Criando o arquivo config.py

```
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criando a engine de conexão

engine = create_engine(DATABASE_URL)

# Criando a sessão

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

```

Criando o arquivo .env


* Para se conectar a este banco de dados PostgreSQL, também vamos usar o SQL Alchemy
    
    ```bash
    postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco
    ```
    
    Isso se estiver se conectando da sua máquina host. Se estiver se conectando de outro contêiner Docker na mesma rede, substitua `localhost` pelo nome do contêiner (`meu_postgres`).

Com este comando, você criará um contêiner PostgreSQL com dados persistentes, que sobreviverão às reinicializações do contêiner e remoções do contêiner. 

### Arquivo config.py



Esse código configura a conexão com um banco de dados PostgreSQL usando SQLAlchemy e python-dotenv, e fornece uma forma de gerenciar sessões de banco de dados em um aplicativo FastAPI. As sessões são essenciais para executar consultas e operações no banco de dados.

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
# Importa funcionalidades do SQLAlchemy: 
# create_engine (para conectar ao banco de dados), 
# Column, Integer, String, Float (para definir colunas e tipos de dados nas tabelas).

from sqlalchemy.orm import sessionmaker, declarative_base
# Importa sessionmaker (para criar sessões de banco de dados) e 
# declarative_base (para criar uma classe base para modelos declarativos).

import os
from dotenv import load_dotenv
# Importa o módulo os para interagir com o sistema operacional e 
# load_dotenv do pacote python-dotenv para carregar variáveis de ambiente de um arquivo .env.

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env.

# Acessa e armazena variáveis de ambiente específicas (credenciais do banco de dados).
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Constrói a URL de conexão do banco de dados usando as variáveis de ambiente.
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Cria um motor de banco de dados SQLAlchemy que gerencia as conexões à base de dados.
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões do SQLAlchemy que será usada para criar sessões.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Cria uma classe base declarativa para os modelos do SQLAlchemy.
Base = declarative_base()

# Define uma função geradora que fornece uma sessão de banco de dados e garante o fechamento da sessão.
def get_db():
    db = SessionLocal()  # Cria uma instância da sessão de banco de dados.
    try:
        yield db  # Fornece a sessão para a operação (utilizado em dependências do FastAPI).
    finally:
        db.close()  # Garante que a sessão seja fechada após o uso.
```

### Arquivo models.py

O arquivo model.py é utilizado em projetos que utilizam o SQLAlchemy, um ORM (Object-Relational Mapping) para Python. Este arquivo define as classes que representam as tabelas do banco de dados em um estilo declarativo. Cada classe mapeia para uma tabela, e cada atributo da classe mapeia para uma coluna na tabela correspondente. Vamos detalhar o código:

```python
from sqlalchemy import Column, Integer, String, Float
# Importa as classes Column, Integer, String e Float do SQLAlchemy.
# Essas classes são usadas para definir as colunas nas tabelas do banco de dados.

from sqlalchemy.orm import declarative_base
# Importa a função declarative_base do SQLAlchemy ORM.
# declarative_base é usado para criar uma classe base para modelos declarativos.

Base = declarative_base()
# Cria uma classe base para modelos declarativos.
# Classes que herdam de Base são automaticamente mapeadas para tabelas.

class Produto(Base):
    # Define uma nova classe Produto, herdando de Base.
    # Esta classe representa uma tabela no banco de dados.

    __tablename__ = "produtos"
    # Define o nome da tabela no banco de dados.
    # Quando uma instância de Produto for salva, ela será armazenada na tabela 'produtos'.

    id = Column(Integer, primary_key=True, index=True)
    # Define uma coluna 'id' como um inteiro, chave primária e indexada.
    # Isso significa que cada produto terá um ID único, que também será usado para indexação.

    titulo = Column(String, nullable=False)
    # Define uma coluna 'titulo' que armazena strings (textos).
    # 'nullable=False' significa que esta coluna não pode ser nula (ou seja, o título é obrigatório).

    descricao = Column(String)
    # Define uma coluna 'descricao' que também armazena strings.
    # Não tem 'nullable=False', portanto, esta coluna pode ser nula (opcional).

    preco = Column(Float, nullable=False)
    # Define uma coluna 'preco' que armazena números de ponto flutuante (decimais).
    # Assim como 'titulo', esta coluna é obrigatória (não pode ser nula).
```

Arquivo schemas.py

O arquivo schemas.py, contendo a definição de ProdutoSchema, é utilizado para definir esquemas de dados usando a biblioteca Pydantic no contexto de uma aplicação FastAPI. Este arquivo é essencial para a validação e documentação de dados de entrada e saída na sua API. Vamos explorar o que cada parte do código faz:

```python
from sqlalchemy import Column, Integer, String, Float
# Importa as classes Column, Integer, String e Float do SQLAlchemy.
# Essas classes são usadas para definir as colunas nas tabelas do banco de dados.

from sqlalchemy.orm import declarative_base
# Importa a função declarative_base do SQLAlchemy ORM.
# declarative_base é usado para criar uma classe base para modelos declarativos.

Base = declarative_base()
# Cria uma classe base para modelos declarativos.
# Classes que herdam de Base são automaticamente mapeadas para tabelas.

class Produto(Base):
    # Define uma nova classe Produto, herdando de Base.
    # Esta classe representa uma tabela no banco de dados.

    __tablename__ = "produtos"
    # Define o nome da tabela no banco de dados.
    # Quando uma instância de Produto for salva, ela será armazenada na tabela 'produtos'.

    id = Column(Integer, primary_key=True, index=True)
    # Define uma coluna 'id' como um inteiro, chave primária e indexada.
    # Isso significa que cada produto terá um ID único, que também será usado para indexação.

    titulo = Column(String, nullable=False)
    # Define uma coluna 'titulo' que armazena strings (textos).
    # 'nullable=False' significa que esta coluna não pode ser nula (ou seja, o título é obrigatório).

    descricao = Column(String)
    # Define uma coluna 'descricao' que também armazena strings.
    # Não tem 'nullable=False', portanto, esta coluna pode ser nula (opcional).

    preco = Column(Float, nullable=False)
    # Define uma coluna 'preco' que armazena números de ponto flutuante (decimais).
    # Assim como 'titulo', esta coluna é obrigatória (não pode ser nula).
```

### Arquivo schemas.py

O arquivo schemas.py, contendo a definição de ProdutoSchema, é utilizado para definir esquemas de dados usando a biblioteca Pydantic no contexto de uma aplicação FastAPI. Este arquivo é essencial para a validação e documentação de dados de entrada e saída na sua API. Vamos explorar o que cada parte do código faz:

```python
from typing import Optional
# Importa o tipo 'Optional' do módulo 'typing'. 
# 'Optional' é usado para indicar campos que podem ser nulos (None).

from pydantic import BaseModel, PositiveFloat
# Importa 'BaseModel' e 'PositiveFloat' do módulo 'pydantic'.
# 'BaseModel' é a classe base para criar esquemas de dados com Pydantic.
# 'PositiveFloat' é um tipo específico do Pydantic para representar números flutuantes positivos.

class ProdutoSchema(BaseModel):
    # Define uma classe 'ProdutoSchema' que herda de 'BaseModel'.
    # Esta classe será usada para criar instâncias de esquemas de dados para produtos,
    # validando e serializando dados de acordo com os tipos definidos.

    """
    Modelo para um item de produto
    """
    # Documentação da classe.

    id: Optional[int] = None
    # Define um campo 'id' como um inteiro opcional (pode ser nulo).
    # O valor padrão é 'None', indicando que o campo pode ser omitido.

    titulo: str
    # Define um campo 'titulo' que deve ser uma string.
    # Este campo é obrigatório (não tem 'Optional').

    descricao: Optional[str] = None
    # Define um campo 'descricao' como uma string opcional.
    # Também pode ser omitido na criação de uma instância da classe.

    preco: PositiveFloat
    # Define um campo 'preco' que deve ser um número de ponto flutuante positivo.
    # É um campo obrigatório.

    class ConfigDict:
        from_attributes = True
    # Isso permitiria que o modelo Pydantic leia dados mesmo se eles forem ORMs do SQLAlchemy ou outros dicionários.
```

Agora o arquivo Router.py

```python
from fastapi import APIRouter, Depends, HTTPException
# Importa classes necessárias do FastAPI: 
# APIRouter (para definir rotas), 
# Depends (para injeção de dependências), 
# HTTPException (para lançar exceções HTTP).

from sqlalchemy.orm import Session
# Importa a classe Session do SQLAlchemy ORM para gerenciar as sessões do banco de dados.

from typing import List
# Importa List do módulo typing para uso em anotações de tipo.

from .schemas import ProdutoSchema
# Importa o esquema ProdutoSchema definido em schemas.py para validação de dados.

from .config import SessionLocal, get_db
# Importa a função get_db e a fábrica de sessão SessionLocal de config.py.

from .model import Produto
# Importa a classe do modelo Produto definida em model.py que mapeia para a tabela de produtos no banco de dados.

router = APIRouter()
# Cria uma instância de APIRouter, que é usada para definir as rotas/endpoints da API.

@router.get("/produtos", response_model=List[ProdutoSchema])
# Define uma rota GET para '/produtos'.
# response_model especifica que a resposta deve ser uma lista de instâncias de ProdutoSchema.
async def listar_produtos(db: Session = Depends(get_db)):
    # Função assíncrona que lista produtos.
    # A sessão do banco de dados é injetada via Depends.
    return db.query(Produto).all()
    # Retorna todas as instâncias de Produto na tabela produtos.

@router.get("/produtos/{produto_id}", response_model=ProdutoSchema)
# Define uma rota GET para '/produtos/{produto_id}'.
# Espera um ID de produto na URL e usa ProdutoSchema para a resposta.
async def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    # Função assíncrona para obter um produto específico pelo ID.
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    # Consulta o produto pelo ID fornecido.
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    # Se o produto existe, retorna-o; senão, lança uma exceção HTTP 404.

# As próximas rotas seguem um padrão similar:
# - A rota POST '/produtos' para inserir um novo produto.
# - A rota DELETE '/produtos/{produto_id}' para remover um produto pelo ID.
# - A rota PUT '/produtos/{produto_id}' para atualizar um produto pelo ID.
```

### Arquivo main.py

```python
from fastapi import FastAPI  # Importa a classe FastAPI do framework FastAPI.
from .router import router  # Importa o objeto 'router' do módulo 'router' local.

app = FastAPI()  # Cria uma instância do aplicativo FastAPI.
# 'app' é a instância central do seu aplicativo web.

app.include_router(router)  # Anexa o roteador 'router' ao aplicativo FastAPI.
# Isso registra todas as rotas e operações definidas em 'router' no aplicativo.
```

### Refatorar os testes

arquivo test_api.py

```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

from pydantic import ValidationError


@pytest.fixture
def test_client():
    """
    Cria uma instância de TestClient que pode ser usada em testes.
    O TestClient é utilizado para simular requisições à API FastAPI.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def produto_id(test_client):
    """
    Fixture que cria um produto na API e retorna o ID desse produto.
    Utilizado para testar operações que necessitam de um produto existente.
    """
    produto_data = {
        "titulo": "Produto Teste",
        "descricao": "Descrição Teste",
        "preco": 19.99,
    }
    response = test_client.post("/produtos", json=produto_data)
    assert response.status_code == 201
    return response.json()["id"]


def test_listar_produtos(test_client):
    """
    Testa se a rota GET '/produtos' retorna uma lista e um status code 200 (sucesso).
    Verifica se a resposta é uma lista, indicando uma listagem bem-sucedida dos produtos.
    """
    response = test_client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_inserir_produto(test_client):
    """
    Testa a criação de um produto através da rota POST '/produtos'.
    Verifica se o produto é criado com sucesso e se os dados retornados são corretos.
    """
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


def test_obter_produto(test_client, produto_id):
    """
    Testa a obtenção de um produto específico através da rota GET '/produtos/{produto_id}'.
    Verifica se o produto obtido corresponde ao produto criado pela fixture 'produto_id'.
    """
    response = test_client.get(f"/produtos/{produto_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == produto_id
    assert "titulo" in data


def test_atualizar_produto(test_client, produto_id):
    """
    Testa a atualização de um produto existente pela rota PUT '/produtos/{produto_id}'.
    Verifica se a atualização é bem-sucedida e se os dados atualizados estão corretos.
    """
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
    """
    Testa a remoção de um produto pela rota DELETE '/produtos/{produto_id}'.
    Verifica se o produto é removido com sucesso e se o mesmo não é mais encontrado após a remoção.
    """
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

```

### Criando um arquivo Docker

* Para se conectar a este banco de dados PostgreSQL, você deve usar obter o endereço IP do container docker
    
    ```bash
    docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' meu_container_postgres
    ```

```bash
docker run -d \
  -e POSTGRES_USER=meu_usuario \
  -e POSTGRES_PASSWORD=minha_senha \
  -e POSTGRES_DB=meu_banco \
  -e DB_HOST=172.17.0.3 \
  -e DB_PORT=5432 \
  -p 8000:8000 \
  --name nome_do_container \
  nome_da_imagem
```

