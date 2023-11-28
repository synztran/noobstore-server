from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from datetime import datetime


class ShippingAt(BaseModel):
    fname: str
    lname: str
    cname: str
    email: EmailStr
    town_city: str
    phone_number: str
    address: str
    country: str
    zip_code: int


class AccountSchema(BaseModel):
    customer_id: int = Field(...)
    account_id: int = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    fname: str = Field(...)
    lname: str = Field(...)
    birth_date: str = Field(...)
    shipping_at: ShippingAt
    phone_area_code: str
    phone_number: str
    created: str
    active: bool = False
    active_date:  datetime
    get_noti: bool = False
    paypal: str
    fb_url: str
    registration_token: str
    expiration_token_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "email": "abc@gmail.com",
                "password": "123456abc",
                "fname": "Hari",
                "lname": "Chan",
                "birth_date": "01/01/2001",
                "shipping_at": {
                    "fname": "A",
                    "lname": "Giang",
                    "cname": "Long",
                    "email": "a.giang@gmail.com",
                    "town_city": "Ho chi minh",
                    "phone_number": "+84 123456789",
                    "address": "53 barker street, Berminham, London",
                    "country": "England",
                    "zip_code": '35000'
                },
                "phone_area_code": "+84",
                "phone_number": "+84 123456789",
                "created": "",
                "active": False,
                "active_date":  None,
                "get_noti": False,
                "paypa": "",
                "fb_url": "",
                "registration_token": "",
                "expiration_token_date": "",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
