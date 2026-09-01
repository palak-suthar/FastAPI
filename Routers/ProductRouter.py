from fastapi import APIRouter, Response
from Models.ProductModels import Product

from Controllers.ProductController import (
    create_product_controller,
    get_products_by_id_controller,
    get_products_controller,
    updateProduct_controller,
    deleteProduct_controller
)

ProductRouter = APIRouter(
    prefix="/products",
    tags=["products"]
)


@ProductRouter.post("/postproduct")
async def create_product(product: Product, response: Response):
    return await create_product_controller(product, response)


@ProductRouter.get("/getproducts")
async def get_products(response: Response):
    return await get_products_controller(response)
    

@ProductRouter.get("/getproduct/{productid}")
async def get_product(productid: str, response: Response):
    return await get_products_by_id_controller(productid, response)


@ProductRouter.put("/product/{productid}")
async def updateProduct(productid: str, product: Product, response: Response):
    return await updateProduct_controller(productid, product, response)


@ProductRouter.delete("/deleteproduct/{productid}")
async def delete_product(productid: str, response: Response):
    return await deleteProduct_controller(productid, response)