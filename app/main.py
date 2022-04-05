from fastapi import FastAPI

from routes import router

app = FastAPI()


@app.get("/")
def get_root():
    return {"msg": "Stock API"}


app.include_router(router, prefix="")
