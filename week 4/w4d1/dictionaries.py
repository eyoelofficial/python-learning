products = [
    {"name": "burger", "price": 300, "stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50}
]
total = 0
for product in products:
    if product["name"] == "burger":
        product["stock"] += 5
    if product["name"] == "pizza":
        product["price"] += 50
    if product["name"] == "cola":
        product["stock"] -= 8
    total += product["price"] * product["stock"]
    print(total)