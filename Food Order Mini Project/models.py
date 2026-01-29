from pydantic import BaseModel

class MenuItem(BaseModel):
    id:int
    name:str
    price: float

class Order(BaseModel):
    item_it: int
    quantity: int