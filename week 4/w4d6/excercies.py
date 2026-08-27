products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15},
    {"name": "tacos", "price": 1850, "stock": 60}
]

has_low_stock = any(product["stock"]<15 for product in products)
print(has_low_stock)
all_prices_valid = all(product["price"]>0 for product in products)
print(all_prices_valid)