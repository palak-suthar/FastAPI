from fastapi import FastAPI
from Routers.ProductRouter import ProductRouter


app = FastAPI()

app.include_router(ProductRouter)

# First Commit 
# Changes Made in Feature Branch jhfj

