products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15},
    {"name": "tacos", "price": 1850, "stock": 60}
    ]

def get_product_price(product):
    return product["price"]

product_price = list(map(get_product_price, products))
print(product_price)

def get_product_value(product):
    return product["price"] * product["stock"]

product_value = list(map(get_product_value, products))
print(product_value)

def get_product_names(product):
    return str.upper(product["name"])

product_names = list(map(get_product_names, products))
print(product_names)
