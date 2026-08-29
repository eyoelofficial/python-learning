products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15},
    {"name": "tacos", "price": 1850, "stock": 60}
    ]

def is_stock_low(product):
    return product["stock"]<25

low_stock = list(filter(is_stock_low,products))
for product in low_stock:
    print(f"{product["name"]}, {product["price"]}, {product["stock"]}")

def is_product_expensive(product):
    return product["price"]>450

expensive_products = list(filter(is_product_expensive,products))
for product in expensive_products:
    print(f"{product["name"]}, {product["price"]}, {product["stock"]}")

