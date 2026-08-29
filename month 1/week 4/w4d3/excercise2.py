products = [
    {"name": "burger","price": 300,"stock": 20},
    {"name": "pizza", "price": 500, "stock": 10},
    {"name": "cola", "price": 60, "stock": 50},
    {"name": "chicken", "price": 850, "stock": 15}
    ]

def view_products():
    for product in products:
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")

def most_expensive_product():
    most_expensive = max(products, key=lambda products: products["price"] )
    print(f" ==> {most_expensive["name"]} | {most_expensive["price"]} | {most_expensive["stock"]} <==")
#
def list_expensive_product():
    list_expensive = min(products, key=lambda products: products["price"] )
    print(f" ==> {list_expensive["name"]} | {list_expensive["price"]} | {list_expensive["stock"]} <==")

def Highest_stock_product():
    most_expensive = max(products, key=lambda products: products["stock"] )
    print(f" ==> {most_expensive["name"]} | {most_expensive["price"]} | {most_expensive["stock"]} <==")
#
def lowest_stock_product():
    list_expensive = min(products, key=lambda products: products["stock"] )
    print(f" ==> {list_expensive["name"]} | {list_expensive["price"]} | {list_expensive["stock"]} <==")

def Sort_products_by_price():
    products_sorted = sorted(products, key=lambda products: products["price"], reverse=True)
    for product in products_sorted:
        print(f"{product['name']} | {product['price']} | {product['stock']}")

def Sort_products_by_stock():
    products_sorted = sorted(products, key=lambda products: products["stock"], reverse=True)
    for product in products_sorted:
        print(f"{product['name']} | {product['price']} | {product['stock']}")
#
def sum_of_products_stock():
    sum_of_stock = sum(product["stock"] for product in products)
    print(sum_of_stock)

def menu():
    print("1. view products")
    print("2. Most expensive product")
    print("3. list expensive product")
    print("4. Highest stock product")
    print("5. lowstest stock product")
    print("6. Sort products by price")
    print("7. Sort products by stock")
    print("8. sum of stock")
    print("9. exit")

while True:
    menu()
    choice = input("choose 1/2/3/4/5/6/7/8/9: ")
    if choice == "1":
        view_products()
    elif choice == "2":
       most_expensive_product() 
    elif choice == "4":
        Highest_stock_product()
    elif choice == "6":
        Sort_products_by_price()
    elif choice == "7":
        Sort_products_by_stock()
    elif choice == "3":
        list_expensive_product()
    elif choice == "5":
        lowest_stock_product()
    elif choice == "8":
        sum_of_products_stock()
    elif choice == "9":
        break
