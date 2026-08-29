products = [
    {"name": "burger", "price": 300, "stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15}
]

low_stock = list(filter(lambda product: product["stock"]<25, products))
print(low_stock)
names = list(map(lambda product: product["name"], low_stock))
print(names)
has_low_stock = any(product["stock"]<20 for product in products)
print(has_low_stock)
all_low_stock = all(product["stock"]>20 for product in products)
print(all_low_stock)
has_out_low_stock = any(product["stock"] == 0 for product in products)
print(has_out_low_stock)