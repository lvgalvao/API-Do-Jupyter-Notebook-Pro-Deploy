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
