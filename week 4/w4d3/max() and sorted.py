products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15}
    ]

for product in products:
    print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
print(" ")
most_expensive = max(products, key=lambda products: products["price"] )
print(f" ==> {most_expensive["name"]} | {most_expensive["price"]} | {most_expensive["stock"]} <==")
print(" ")
products_sorted = sorted(products, key=lambda products: products["price"], reverse=True)
for product in products_sorted:
    print(f"{product['name']} | {product['price']} | {product['stock']}")
    