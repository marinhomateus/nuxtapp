from pydantic import BaseModel

class Stock(BaseModel):
    id: int
    name: str
    ticker: str
    company_code: str