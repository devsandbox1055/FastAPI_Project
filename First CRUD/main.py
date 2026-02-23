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
# read or fetch all data(DATA WEBSITE PE DIKHAANE KE LIYE)

@app.get("/product")
async def all_product():
    return PRODUCTS

# Product mein se ek ka product ka sirf data read karne ke liye
@app.get("/product/{product_id}")
async def single_product(product_id:int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product    #jo product_id hamlog denege to vo product id jo hamne data diya hai 
        #usse match karega..agar vo dono same huye to Products mein se uss single product ka poora 
        #detail nikaal ke de dega

# POST REQUEST
# CREATE OR INSERT DATA
@app.post("/product")
async def create_data(new_product: dict):
    PRODUCTS.append(new_product)
    return {"status":"created" , "new_product": new_product}

# PUT request
# update complete data in dict
@app.put("/product/{product_id}")
def update_product(product_id:int , new_updated_product: dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[INDEX] = new_updated_product
            return {"status":"updated" , "product_id": product_id,"new updated product": new_updated_product}


#Patch request
# UPDATE PARTIAL DATA

@app.patch("/product/{product_id}")
def partial_product(product_id: int , new_updated_product:dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(new_updated_product)
            return {"status":"Partial updated" , "product_id": product_id,"new updated product": product}

# Delete request
# delete data
@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    for index,product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"response": "Data Deleted", "product_id":product_id}


                