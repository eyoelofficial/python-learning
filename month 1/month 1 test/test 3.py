products = [
    {"name": "rice", "price": 120, "stock": 80},
    {"name": "beef", "price": 650, "stock": 15},
    {"name": "chicken", "price": 500, "stock": 30},
    {"name": "oil", "price": 300, "stock": 8},
    {"name": "milk", "price": 90, "stock": 45},
    {"name": "coffee", "price": 250, "stock": 0}
]
def calculate_number_of_products(products):
    calculate_number=len(products)
    print(f"products: {calculate_number}")
def number_of_total_stock(products):
    total_stock=sum(product["stock"] for product in products)
    print(f"total stock: {total_stock}")
def total_inventory_value(products):
    inventory_value=0
    for product in products:
        inventory_value+= product["price"]*product["stock"]
    print(f"Inventory value: {inventory_value}")
def most_expenice_price(products):
    most_expenice=max(products, key=lambda product: product["price"])
    print(f"Most expenice: {most_expenice["name"]}")
def highest_stock_product(products):
    highest_stock=max(products, key=lambda product: product["stock"])
    print(f"highest stock: {highest_stock["name"]}")
def lowest_stock_product(products):
    lowest_stock=min(products, key=lambda product: product["stock"])
    print(f"lowest stock: {lowest_stock["name"]}")
def low_stock_products(products):
    low_stock= list(filter(lambda product: product["stock"]<20, products))
    low_stock_names= list(map(lambda product: product["name"], low_stock))
    print("Low-stock products: ")
    for product in low_stock_names:
        print(" " + product)
def zero_stock_products(products):
    zero_stock= list(filter(lambda product: product["stock"]==0, products))
    zero_stock_names= list(map(lambda product: product["name"], zero_stock))
    print("Low-stock products: ")
    for product in zero_stock_names:
        print(" " + product)
pass
def inventory_analaysis(products):
    print("========== INVENTORY ANALYSIS ==========")
    calculate_number_of_products(products)
    number_of_total_stock(products)
    total_inventory_value(products)
    print("")
    most_expenice_price(products)
    highest_stock_product(products)
    lowest_stock_product(products)
    print("")
    low_stock_products(products)
    zero_stock_products(products)
    print("========================================")
inventory_analaysis(products)