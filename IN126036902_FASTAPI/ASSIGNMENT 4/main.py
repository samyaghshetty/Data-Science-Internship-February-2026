from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# List of available products in the store with their details
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "in_stock": True}
]

# Temporary storage for cart and orders in memory (not persistent)
cart = []
orders = []
order_id = 1


# Function to calculate subtotal price for a cart item
def calculate_total(price, quantity):
    return price * quantity


# Endpoint to add products to the cart with quantity
@app.post("/cart/add")
def add_to_cart(product_id: int, quantity: int = 1):

    # Find the product from the product list based on the provided product_id
    product = next((p for p in products if p["id"] == product_id), None)

    # If product does not exist 
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # If product is out of stock 
    if not product["in_stock"]:
        raise HTTPException(status_code=400, detail=f"{product['name']} is out of stock")

    # Check if product already exists in cart 
    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            item["subtotal"] = calculate_total(product["price"], item["quantity"])

            return {
                "message": "Cart updated",
                "cart_item": item
            }

    # If product is not already in cart, add new item to cart
    subtotal = calculate_total(product["price"], quantity)

    cart_item = {
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "subtotal": subtotal
    }

    cart.append(cart_item)

    return {
        "message": "Added to cart",
        "cart_item": cart_item
    }


# Endpoint to view cart items and calculate total price
@app.get("/cart")
def view_cart():

    # If cart is empty  
    if not cart:
        return {"message": "Cart is empty"}

    # Calculate total price of cart 
    grand_total = sum(item["subtotal"] for item in cart)

    return {
        "items": cart,
        "item_count": len(cart),
        "grand_total": grand_total
    }


# Endpoint to remove item from cart based on product_id
@app.delete("/cart/{product_id}")
def remove_item(product_id: int):

    for item in cart:
        if item["product_id"] == product_id:
            cart.remove(item)
            return {"message": "Item removed"}

    raise HTTPException(status_code=404, detail="Item not found in cart")


# Request body model for checkout information
class Checkout(BaseModel):
    customer_name: str
    delivery_address: str


# Endpoint to checkout the cart and create orders based on cart items
@app.post("/cart/checkout")
def checkout(data: Checkout):

    global order_id

    # Prevent checkout if cart is empty  
    if not cart:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty — add items first"
        )

    created_orders = []

    # Create orders from cart items 
    for item in cart:
        order = {
            "order_id": order_id,
            "customer_name": data.customer_name,
            "product": item["product_name"],
            "quantity": item["quantity"],
            "total_price": item["subtotal"]
        }

        orders.append(order)
        created_orders.append(order)
        order_id += 1

    # Calculate total order value 
    grand_total = sum(order["total_price"] for order in created_orders)

    # Clear cart after checkout 
    cart.clear()

    return {
        "message": "Order placed successfully",
        "orders_placed": created_orders,
        "grand_total": grand_total
    }


# Endpoint to view all orders placed in the system
@app.get("/orders")
def get_orders():

    return {
        "orders": orders,
        "total_orders": len(orders)
    }
