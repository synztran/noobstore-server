from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_products,
    add_product
)
# from app.server.models.student import (
from server.models.product import (
    ErrorResponseModel,
    ResponseModel,
    ProductSchema,
)

router = APIRouter()

# Retrieve all acount


@router.get("", response_description="Products data from the database")
async def get_all_product():
    products = await retrieve_products()
    if products:
        return ResponseModel(products, "Products data retrieve successfully")
    return ResponseModel(products, "Empty list returned")


@router.post("", response_description="Product data added into the database")
async def add_product_data(product: ProductSchema = Body(...)):
    product = jsonable_encoder(product)
    new_product = await add_product(product)
    return ResponseModel(new_product, "Product added successfully.")

# @router.post("/", response_description="Account data added into the database")
# async def add_account_data(account: AccountSchema = Body(...)):
#     account = jsonable_encoder(account)
#     new_account = await add_account(account)
#     return ResponseModel(new_account, "Student added successfully.")
