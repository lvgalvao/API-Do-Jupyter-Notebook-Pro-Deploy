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
