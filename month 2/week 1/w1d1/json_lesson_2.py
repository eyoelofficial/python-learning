import json
with open("products.json","r")as file:
    loaded_products=json.load(file)
    print("loaded")  
def change_name():
    for product in loaded_products:
        new_name = (input("input new name: "))
        product["name"] = new_name
        print("updated")
        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
        save_products() 
def save_products():
    with open("products.json","w") as file:
        json.dump(loaded_products, file, indent=1)
    print("saved")
def wrong():
    print(" Invalid ")
def search():
    while True:
        for product in loaded_products:
            print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
        print(" do u want to edit anything?. y/n")
        choice = input(": ")
        found = False
        if choice == "y":
            change_product=input("name: ")
            for product in loaded_products:
                if change_product == product["name"]:
                    found = True
                    print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
                    what=input("what do u wnat to change? name/price/stock: ")
                    if what == "name":
                        new_name = (input("input new name: "))
                        product["name"] = new_name
                        print("updated")
                        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
                        save_products()
                    elif what == "price":
                        new_price = int(input("input new price: "))
                        product["price"] = new_price
                        print("updated")
                        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
                        save_products()
                    elif what == "stock":
                        new_stock = int(input("input new stock: "))
                        product["stock"] = new_stock
                        print("updated")
                        print(f"{product["name"]} | {product["price"]} | {product["stock"]}")
                        save_products()
                    else:
                        wrong()
                    if found == False:
                        wrong()
                else:
                    wrong()
        elif choice == "n":
            break
        else:
            wrong()
search()