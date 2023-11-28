from typing import List
from pydantic import BaseModel, Field
from enum import Enum


class StatusGB(Enum):
    END = 0
    IC = 1
    LIVE = 2


class CategoryType(Enum):
    Keeb = 0
    Keycap = 1
    ETC = 2


class Image(BaseModel):
    path: str
    size: float


class CategorySchema(BaseModel):
    category_id: str = Field(...)
    category_url_name: str
    category_name: str
    manufacturing: str
    author: str
    proxy_host: str
    status_gb: StatusGB
    type: CategoryType
    date_start: str
    date_end: str
    date_payment: str
    min_price: int
    max_price: int
    tax: int
    handle: int
    thumbnail: Image
    image_list: List[Image]
    content: str
    time_line: None

    class Config:
        schema_extra = {
            "example": {
                "category_id": 'abc',
                "category_url_name": "123456abc",
                "category_name": "Hari",
                "manufacturing": "Chan",
                "author": "A Lu",
                "proxy_host": "text",
                "status_gb": 0,
                "type": 0,
                "date_start": '',
                "date_end": '',
                "date_payment": '',
                "min_price": 0,
                "max_price": 0,
                "tax": 0,
                "handle": 0,
                "thumbnail": {
                    "path": "",
                    "size": 0
                },
                "image_list": [{"paht": "", "size": 0}],
                "content":  "",
                "get_noti": False,
                "time_line": {}
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
