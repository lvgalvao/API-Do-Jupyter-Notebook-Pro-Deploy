from typing import Optional
from pydantic import BaseModel, PositiveFloat


class ModeloItem(BaseModel):
    """
    Modelo para um item de produto
    """

    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat
