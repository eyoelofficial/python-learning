import json
products = [
    {"name": "rice", "price": 180, "stock": 60},
    {"name": "beef", "price": 650, "stock": 15},
    {"name": "milk", "price": 90, "stock": 45}
]
with open("products.json","w") as file:
    json.dump(products, file, indent=4)
    print("done")
with open("products.json","r")as file:
    loaded_products=json.load(file)
    for product in loaded_products:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
    print("done again")
