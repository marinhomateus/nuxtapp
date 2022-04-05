from fastapi import APIRouter

from models.stock import Stock

router = APIRouter()

db = []

@router.post("/")
def add_item(item: Stock):
    db.append(item)
    return item

@router.get("/")
def list_items():
    return db