products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15},
    {"name": "tacos", "price": 1850, "stock": 60}
    ]

def view_products():
    for product in products:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
    print("--------------------------------------")

def Most_expensive_product():
    Most_expensive_product_list=[product for product in products if product["price"]>450]
    for product in Most_expensive_product_list:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
    print("--------------------------------------")

def list_expensive_products():
    list_expensive_product_list=[product for product in products if product["price"]<450]
    for product in list_expensive_product_list:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
    print("--------------------------------------")

def high_stock_products():
    high_stock_products_list=[product for product in products if product["stock"]>25]
    for product in high_stock_products_list:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
    print("--------------------------------------")

def low_stock_products():
    low_stock_products_list=[product for product in products if product["stock"]<25]
    for product in low_stock_products_list:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
    print("--------------------------------------")

def name_of_products():
    name_of_products_list=[product["name"] for product in products]
    for product in name_of_products_list:
            print(product)
    print("--------------------------------------")       

def names_most_expensive_product():
    names_most_expensive_product_list=[product["name"] for product in products if product["price"]>450]
    for product in names_most_expensive_product_list:
        print(product)
    print("--------------------------------------")

def menu():
    print("1. view products \n" \
    "2. Most expensive product\n" \
    "3. list expensive products\n" \
    "4. high stock products\n" \
    "5. low stock products\n" \
    "6. names of products \n" \
    "7. names of expenive products \n" \
    "8. exit")

while True:
    menu()
    choice = input("1/2/3/4/5/6/6/7/8: ")
    if choice == "1":
        view_products()
    elif choice == "2":
        Most_expensive_product()
    elif choice == "3":
        list_expensive_products()
    elif choice == "4":
        high_stock_products()
    elif choice == "5":
        low_stock_products()
    elif choice == "6":
        name_of_products()
    elif choice == "7":
        names_most_expensive_product()
    elif choice == "8":
        break