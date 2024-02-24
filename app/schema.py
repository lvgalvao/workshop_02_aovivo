import pandera as pa
from pandera.typing import DataFrame, Series


class ProdutoSchema(pa.SchemaModel):
    id_produto: Series[int]
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=05.0, le=120.0)
    categoria: Series[str]

    class Config:
        coerce = True