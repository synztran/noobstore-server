from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    # add_student,
    # delete_student,
    # retrieve_student,
    # retrieve_students,
    # update_student,
    retrieve_accounts,
    add_account
)
# from app.server.models.student import (
from server.models.account import (
    ErrorResponseModel,
    ResponseModel,
    AccountSchema,
    # UpdateStudentModel,
)

router = APIRouter()

# Retrieve all acount


@router.get("", response_description="Account data from the database")
async def get_all_account():
    accounts = await retrieve_accounts()
    if accounts:
        return ResponseModel(accounts, "Accounts data retrieve successfully")
    return ResponseModel(accounts, "Empty list returned")


@router.post("", response_description="Account data added into the database")
async def add_account_data(account: AccountSchema = Body(...)):
    account = jsonable_encoder(account)
    new_account = await add_account(account)
    return ResponseModel(new_account, "Account added successfully.")

# @router.post("/", response_description="Account data added into the database")
# async def add_account_data(account: AccountSchema = Body(...)):
#     account = jsonable_encoder(account)
#     new_account = await add_account(account)
#     return ResponseModel(new_account, "Student added successfully.")
