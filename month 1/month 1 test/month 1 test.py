products = [
    {"name": "burger", "price": 600, "stock": 100},
    {"name": "tacos", "price": 800, "stock": 20},
    {"name": "chicken", "price": 850, "stock": 50},
    {"name": "pizza", "price": 400, "stock": 10},
    {"name": "cola", "price": 60, "stock": 600}
]
#1
print("1")
has_low_stock = list(filter(lambda product: product["stock"]<25, products))
has_low_stock_name = list(map(lambda product: product["name"], has_low_stock ))
print(has_low_stock_name)
#2
print("2")
list_with_only_names = list(map(lambda product: product["name"], products))
print(list_with_only_names)
#3
print("3")
expensive_product= any(product["price"]>800 for product in products)
print(expensive_product)
#4
print("4")
does_every_product_have_stock = all(product["stock"]>0 for product in products)
print(does_every_product_have_stock)
#5
print("5")
heighest_price_product = max(products, key=lambda product: product["price"])
print(heighest_price_product["name"])
#6
print("6")
sorted_products_by_price_h2l= sorted(products, key=lambda product: product["price"], reverse=True)
names_sorted_products_by_price_h2l = list(map(lambda product: product["name"], sorted_products_by_price_h2l))
print(names_sorted_products_by_price_h2l)
#7
print("7")
names = ["burger", "tacos", "chicken", "pizza", "cola"]
prices = [600, 800, 850, 400, 60]
new_products_list=list(zip(names,prices))
for name,price in new_products_list:
    print(f"{name} | {price}")
