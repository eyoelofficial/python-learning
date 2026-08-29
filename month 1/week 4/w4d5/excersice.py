products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15},
    {"name": "tacos", "price": 1850, "stock": 60}
    ]

def view_products():
    for product in products:
        print(f"{product["name"]} |{product["price"]} |{product["stock"]} ")

def filter_low_stock(product):
    return product["stock"]<25

low_stock = list(filter(filter_low_stock, products))
for product in low_stock:
    print(f"{product["name"]} |{product["price"]} |{product["stock"]} ")

def map_names(product):
    return product["name"]

name = list(map(map_names,products))
print(name)

name2 = list(map(map_names,low_stock))
print(name2)

#
def filter_low_stock(product):
    return product["stock"]<25

low_stock = list(filter(filter_low_stock, products))

def map_names(low_stock):
    return low_stock["name"]

answer = list(map(map_names,low_stock))
print(answer)
#
def filter_low_stock(product):
    return product["stock"]<25

def map_names(low_stock):
    return low_stock["name"]

answer2 = list(map(map_names, filter(filter_low_stock, products)))
print(answer2)