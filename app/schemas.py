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
