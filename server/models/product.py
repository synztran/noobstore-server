from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class ProductPart(Enum):
    KEEB_TOP_CASE = 0,
    KEEP_BOT_CASE = 1,
    KEEP_PLATE = 2,
    KEEP_FAME = 3,
    KEYCAP = 4,
    SWITCH = 5,
    ARTISAN = 6,
    ETC = 7


class Material(Enum):
    ABS = 0,
    PBT = 1,
    POM = 2,
    FR4 = 3,
    TBD = 5


class IImage(BaseModel):
    path: str
    size: float


class ProductSchema(BaseModel):
    product_id: str = Field(...)
    product_name: str
    replace_product_name: str
    category_id: str
    category_url_name: str
    # product_accessory: 0 = Keeb Top Case | 1 = Keeb Bot case | 2 = Keeb Plate | 3 = Keeb Frame | 4 = keycap | 5 = switches | 7 = artisan | 8 = etc
    product_part: ProductPart = None
    outstock: bool = False
    c_code_color: List[str]
    c_profile: str
    c_material: Material = Material.TBD
    k_top_color: str
    k_top_material: str
    k_bot_color: str
    k_bot_material: str
    k_plate_option: str
    k_plate_material: str
    price: float
    pic_product: IImage
    pic_list: List[IImage]
    specs: str

    class Config:
        schema_extra = {
            "example": {

            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
