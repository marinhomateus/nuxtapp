from fastapi import APIRouter

from models.stock import Stock

router = APIRouter()


@router.post("/")
async def add_item(item: Stock):
    await item.save()
    return item

@router.get("/")
async def list_items():
    return await Papel.objects.all()