products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15},
    {"name": "tacos", "price": 1850, "stock": 60}
    ]

expensive = list(filter(lambda product: product["price"]>450, products))
for product in expensive:
    print(f"{product["name"]} |{product["price"]} |{product["stock"]} ")

product_value = list(map(lambda product: product["price"]*product["stock"], products))
for product in product_value:
    print(product)

product_stock = list(filter(lambda product: product["stock"]<25, products),)
product_name=list(map(lambda product: product["name"], product_stock))
for product in product_name:
    print(product)