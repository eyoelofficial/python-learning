products = [
    {"name": "burger", "price": 300, "stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50}
]
def view_products():
    for product in products:
            print(f"{product["name"]} | {product["price"]} | {product["stock"]}")

#fix
def Search():
    product_name = input("input name: ")
    for product in products:
        if product.get("name") == product_name:
            print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
                

def Restock():
    product_name = input("input name: ")
    product_stock = int(input("input stock"))
    for product in products:
        if product_name == product["name"]:
            product["stock"] += product_stock
            print(f"{product_name} is restoked with {product_stock}.")

def sell():
    product_name = input("input name: ")
    product_stock = int(input("input stock"))
    for product in products:
        if product_name == product["name"]:
            product["stock"] -= product_stock
            print(f"{product_name} is sold with {product_stock}.")

def Product_value():
    product_name = input("input name: ")
    for product in products:
        if product_name == product["name"]:
            product_value = product["price"] * product["stock"]
            print(f"product value = {product_value}")

def total_Product_value():
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
        print(f"product value = {total}")

def menu():
    print("1. view products")
    print("2. search")
    print("3. restock")
    print("4. sell")
    print("5. Product value")
    print("6. total Product value")
    print("7. exit")

while True:
    menu()
    choice = input("1/2/3/4/5/6/7: ")
    if choice == "1":
        view_products()
    elif choice == "2":
        Search()
    elif choice == "3":
        Restock()
    elif choice == "4":
        sell()
    elif choice == "5":
        Product_value()
    elif choice == "6":  
        total_Product_value()
    elif choice == "7":
        break
