products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15}
    ]

for product in products:
    print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
print(" ")
new_list = []

for product in products:
    if product["price"] > 450:
        new_list.append(product)
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
print("1")

second_new_list = [product for product in products if product["stock"] < 20]
for product in second_new_list:
    print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
print("2")

product_name =[]
for product in products:
    product_name.append(product["name"])
print(product_name)
print("3")

second_product_name = [product["name"] for product in products]
print(second_product_name)
print("4")

expenive_product_name = []
for product in products:
    if product["price"]>450:
        expenive_product_name.append(product["name"])
print(expenive_product_name)
print("5")

seconed_expenive_product_name =[product["name"] for product in products if product["price"]>450]
print(seconed_expenive_product_name)
print("6")