import csv
products = [
    {"name": "rice", "price": 180, "stock": 60},
    {"name": "beef", "price": 650, "stock": 15},
    {"name": "milk", "price": 90, "stock": 45},
    {"name": "coffee", "price": 250, "stock": 0 },
    {"name": "chicken", "price": 900, "stock": 10 }
]
with open("new_products.csv", "w") as file:
    fieldname=["name","price","stock"]
    writer=csv.DictWriter(file, fieldname)
    writer.writeheader()
    for product in products:
        writer.writerow(product)
    print("done?mabye now?")