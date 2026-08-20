
products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10}
    ]

#search
def find_product(products, name):
    for product in products:
        if name == product["name"]:
            return product
    return None

# Calculate product value
def Calculate_product_value(price, stock):
    value = price * stock
    return value

# Restock
def Restock(product, amount):
    product["stock"] += amount

#sell
def sell(product, amount): 
    product["stock"] -= amount

def product_value_by_name(products, name):
    product = find_product(products, name)
    if product is not None:
        value = Calculate_product_value(product['price'],product['stock'])
        print(value)
    else:
        print("product not found")

def restock_product_by_name(products, name, amount):
    product = find_product(products, name)
    if product is not None:
        Restock(product, amount)
    else:
       print("product not found")


def sell_product_by_name(products, name, amount):
    product = find_product(products, name)
    if product is not None:
        sell(product, amount)
    else:
       print("product not found")

def menu():
    print("======menu========")
    print("1. View products")
    print("2. Search product")
    print("3. Restock")
    print("4. Sell")
    print("5. Product value")
    print("6. Exit")

while True:
    menu()
    choice = input("choose 1/2/3/4/5/6: ")
    if choice == "1":

            pass
    elif choice == "2":
        pass
    elif choice == "3":
        name = input("Enter product name: ")
        amount = int(input("Enter amount: "))
        restock_product_by_name(products, name, amount)

    elif choice == "4":
        name = input("Enter product name: ")
        amount = int(input("Enter amount: "))
        sell_product_by_name(products, name, amount)

    elif choice == "5":
        name = input("Enter product name: ")
        product_value_by_name(products, name)

    elif choice == "6":
        break