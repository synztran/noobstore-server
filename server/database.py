import motor.motor_asyncio

from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb+srv://admin:123456Ban@cluster0.u7ysm.mongodb.net/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)


database = client.testmongodb

account_collection = database.get_collection("accounts")
category_collection = database.get_collection("categories")
product_collection = database.get_collection("products")

# utils


async def generate_id(collection: str):
    switcher = {
        "account": {
            "collection": account_collection,
            "field": "customer_id",
        },
        "category": {
            "collection": category_collection,
            "field": "category_id"
        },
        "product": {
            "collection": product_collection,
            "field": "product_id"
        }
    }

    generate_collection = switcher.get(collection, "nothing").collection
    generate_field = switcher.get(collection, "nothing").field

    max_id = await generate_collection.find_one(sort=[generate_field, -1])

    if max_id:
        print("max customer id", max_id[generate_field] + 1)
        return max_id[generate_field] + 1
    else:
        return 1

# account


async def generate_customer_id():
    # Find the maximum customer_id from existing documents
    max_customer_id = await account_collection.find_one(sort=[("customer_id", -1)])
    if max_customer_id:
        print("max customer id", max_customer_id["customer_id"] + 1)
        return max_customer_id["customer_id"] + 1
    else:
        # no existing documents, start from 1
        return 1


async def generate_account_id():
    # Find the maximum account_id from existing documents
    max_account_id = await account_collection.find_one(sort=[("account_id", -1)])
    if max_account_id:
        print("max_account_id", max_account_id["account_id"] + 1)
        return max_account_id["account_id"] + 1
    else:
        # No existing documents, start from 1
        return 1


def account_helper(account) -> dict:
    # Can't using async on this func => make Internal Server
    if "active_date" in account:
        # Check if the value of "active_date" is a string
        if isinstance(account["active_date"], str):
            formatActiveDate = account["active_date"]
        else:
            formatActiveDate = ""
    else:
        formatActiveDate = ""

    return {
        "fname": account["fname"],
        "lname": account["lname"],
        "email": account["email"],
        "shipping_at": account["shipping_at"],
        "phone_number": account["phone_number"],
        "active": account["active"],
        "phone_area_code": account["phone_area_code"],
        "created":  account["created"],
        "active": account["active"],
        "active_date":   formatActiveDate,
        "get_noti": account["get_noti"],
        "paypal":  account["paypal"],
        "fb_url":  account["fb_url"],
        # "registration_token":  account["registration_token"],
        # "expiration_token_date":  account["expiration_token_date"],
    }

# Retrieve all accounts present in the database


async def retrieve_accounts():
    accounts = []
    async for account in account_collection.find():
        accounts.append(account_helper(account))
    return accounts

# Add a new student into to the database


async def add_account(account_data: dict) -> dict:
    account_id = await generate_account_id()
    customer_id = await generate_customer_id()
    account_data["account_id"] = account_id
    account_data["customer_id"] = customer_id
    print(account_id, customer_id)
    account = await account_collection.insert_one(account_data)
    new_account = await account_collection.find_one({"_id": account.inserted_id})
    return account_helper(new_account)


# category

def category_helper(category) -> dict:
    return {
        "category_id": category["category_id"]
    }


async def retrieve_categories():
    categories = []
    async for category in category_collection.find():
        categories.append(category_helper(category))
    return categories


async def add_category(category_data: dict) -> dict:
    category_id = await generate_id("category")
    category_data["category_id"] = category_id
    print(category_id)
    category = await category_collection.insert_one(category_data)
    new_category = await category_collection.find_one({"_id": category.inserted_id})
    return category_helper(new_category)


# product

def product_helper(product) -> dict:
    # Can't using async on this func => make Internal Server

    return {
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "replace_product_name": product["replace_product_name"],
        "category_id": product["category_id"],
        "category_url_name": product["category_url_name"],
        "product_part": product["product_part"],
        "outstock": product["outstock"],
        "c_code_color": product.get("c_code_color", ""),
        "c_profile": product.get("c_profile", ""),
        "c_material": product.get("c_material", ""),
        "k_top_color": product.get("k_top_color", ""),
        "k_top_material": product.get("k_top_material", ""),
        "k_bot_color": product.get("k_bot_color", ""),
        "k_bot_material": product.get("k_bot_material", ""),
        "k_plate_option": product.get("k_plate_option", ""),
        "k_plate_material": product.get("k_plate_material", ""),
        "price": product["price"],
        "pic_product": product["pic_product"],
        "pic_list": product.get("pic_list", []),
        "specs": product["specs"],
    }


async def retrieve_products():
    products = []
    async for product in product_collection.find():
        products.append(product_helper(product))
    return products


async def add_product(product_data: dict) -> dict:
    product_id = await generate_id("product")
    product_data["product_id"] = product_id
    print(product_id)
    product = await product_collection.insert_one(product_data)
    new_product = await product_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_product)
