from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    valor: float

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def add_item(new_item: Item):
    return new_item