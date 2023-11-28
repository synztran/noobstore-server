from fastapi import FastAPI

from server.routers.account import router as AccountRouter
from server.routers.category import router as CategoryRouter
from server.routers.product import router as ProductRouter

app = FastAPI()

app.include_router(AccountRouter, tags=["Account"], prefix="/account")
app.include_router(CategoryRouter, tags=["Category"], prefix="/category")
app.include_router(ProductRouter, tags=["Product"], prefix="/product")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
