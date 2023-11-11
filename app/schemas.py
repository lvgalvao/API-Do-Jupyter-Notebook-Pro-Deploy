from typing import Optional
from pydantic import BaseModel, PositiveFloat


class ProdutoSchema(BaseModel):
    """
    Modelo para um item de produto
    """

    id: Optional[int] = None
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat

    class ConfigDict:
        from_attributes = True
