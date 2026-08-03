products = [{"name":"burger","price":250,"stock":10},
            {"name":"pizza","price":350,"stock":15},
            {"name":"chips","price":150,"stock":10},
            {"name":"pasta","price":230,"stock":13}
            ]
def menu():
    print("===menu===")
    print("1. View inventory")
    print("2. Search product")
    print("3. Change stock")
    print("4. total inventory value")
    print("5. Exit")
def View_inventory():
    for product in products:
        print(product)
def Search_product(search):
    try:
        for product in products:
            if product["name"] == search:
                print(product)
    except ValueError:
        print(" product not found")
def Change_stock(product_name,new_stock):
    for product in products:
                for product in products:
                    if product["name"] == product_name:
                        product["stock"] = new_stock
                        print(product)
    else:
        print(" product not found")
def total_inventory_value():
    for product in products:
        answer =product["price"]*product["stock"]
        print (answer)
        total = 0
    for product in products:
        total += product["price"]*product["stock"]
        print (total)
