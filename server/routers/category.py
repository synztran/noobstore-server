from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_categories
)

from server.models.category import (
    ErrorResponseModel,
    ResponseModel,
    CategorySchema
)

router = APIRouter()

# Retrieve all category


@router.get("", response_description="Category data from the db")
async def get_all_category():
    categories = await retrieve_categories()
    if categories:
        return ResponseModel(categories, "Categories data retrieve successfully")
    return ResponseModel(categories, "Empty list returned")


@router.post("", response_description="Category data added into the database")
async def add_category_data(category: CategorySchema = Body(...)):
    category = jsonable_encoder(category)
    new_category = await add_account(category)
    return ResponseModel(new_account, "Account added successfully.")
