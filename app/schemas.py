from enum import Enum
from typing import Optional
from pydantic import BaseModel, PositiveFloat


# Define o Enum para categorias
class Categoria(Enum):
    ELETRONICO = "eletronico"
    CURSO = "curso"
    ALIMENTO = "alimento"


class ProdutoSchema(BaseModel):
    """
    Modelo para um item de produto
    """

    id: Optional[int] = None
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    categoria: Optional[Categoria]
    # Adiciona o campo 'categoria', que deve ser um valor do Enum 'Categoria'

    class Config:
        orm_mode = True
        # Habilita o modo ORM para facilitar a integração com ORMs como SQLAlchemy
