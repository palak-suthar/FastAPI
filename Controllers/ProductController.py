from fastapi import Response
from Models.ProductModels import Product
from dbConnect import products_collection
from bson import ObjectId
from bson.errors import InvalidId


async def create_product_controller(product: Product, response: Response):

    try:
        result =  await products_collection.insert_one(product.dict())
        product.id = str(result.inserted_id)
        return {
            "isSuccess": True,
            "message": "Product created successfully",
            "product": product
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error creating product",
            "isSuccess": False
        }


async def get_products_controller(response: Response):
    try:
        productss = []
        async for product in products_collection.find():
            productss.append(Product(**product))
        return {
            "isSuccess": True,
            "products": productss
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error fetching products",
            "isSuccess": False
        }


async def get_products_by_id_controller(product_id: str, response: Response):
    try:
        product = await products_collection.find_one({"_id": ObjectId(product_id)})
        if product:
            return {"product": Product(**product), "isSuccess": True}
        else:
            response.status_code = 404
            return {'message': 'Product not found', 'isSuccess': False}
    except InvalidId:
        response.status_code = 400
        return {'message': 'Invalid product ID format', 'isSuccess': False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {'message': 'Error Fetching product', 'isSuccess': False}


async def updateProduct_controller(productid: str, product: Product, response: Response):
    try:
        result = await products_collection.update_one(
            {"_id": ObjectId(productid)},
            {"$set": product.dict()}
        )
        if result.modified_count == 1:
            response.status_code = 200
            return {"isSuccess": True, "message": "Product Updated successfully"}
        else:
            response.status_code = 404
            return {"isSuccess": False, "message": "Product not found"}
    except InvalidId:
        response.status_code = 400
        return {"message": "Invalid product ID format", "isSuccess": False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error updating product",
            "isSuccess": False
        }


async def deleteProduct_controller(productid: str, response: Response):
    try:
        result = await products_collection.delete_one({"_id": ObjectId(productid)})
        if result.deleted_count == 1:
            response.status_code = 200
            return {"isSuccess": True, "message": "Product deleted successfully"}
        else:
            response.status_code = 404
            return {"isSuccess": False, "message": "Product not found"}
    except InvalidId:
        response.status_code = 400
        return {'message': 'Invalid product ID format', 'isSuccess': False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {'message': 'Error deleting product', 'isSuccess': False}

    