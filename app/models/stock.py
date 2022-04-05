import ormar
from config import database, metadata


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Stock(ormar.Model):
    class Meta(BaseMeta):
        tablename = "stocks"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    ticker: str = ormar.String(max_length=10)
    company_code: str = ormar.String(max_length=20)
