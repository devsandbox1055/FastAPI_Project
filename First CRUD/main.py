from fastapi import FastAPI

app = FastAPI()

PRODUCTS = [
    {
        "id": 1,
        "title":"dev",
        "price": 99,
        "description" :"your first pack"
    },
    {
        "id": 2,
        "title":"maddy",
        "price": 98,
        "description" :"your second pack"
    },
    {
        "id": 3,
        "title":"diksha",
        "price": 97,
        "description" :"your third pack"
    },

]

# GET request
# read or fetch all data

@app.get("/product")
async def all_product():
    return PRODUCTS