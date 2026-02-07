from fastapi import APIRouter, HTTPException
from app.models import MenuItem, Order

router = APIRouter()

menu_db = {
    1: {"id": 1, "name": "Burger", "price": 120},
    2: {"id": 2, "name": "Pizza", "price": 250},
    3: {"id": 3, "name": "Momos", "price": 80}
}

orders =[]

@router.get("/menu")
def get_menu():
    return list(menu_db.values())

@router.post("/order")
def place_order(order:Order):
    if order.item_id not in menu_db:
        raise HTTPException(status_code=404, detail="item not availabe")
    
    if order.quantity <=0:
        raise HTTPException(status_code=400, detail= "Quantity must be greater then zero")
    

    item = menu_db[order.item_id]
    total_price = item["price"] * order.quantity

    orders.append({
        "item": item["name"],
        "quantity": order.quantity,
        "total_price": total_price
    })

    return {
        "message":"order placed successfully",
        "order":orders[-1]
    }
@router.get("/orders")
def get_orders():
    return orders