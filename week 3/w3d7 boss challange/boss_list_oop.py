# class
class Products:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

    def display(self):
        print(f"Name: {self.name}")
        print(f"Stock: {self.stock}")
        print(f"Price: {self.price}")

    def restock(self, amount):
        self.stock += amount

    def sell(self, amount):
        self.stock -= amount
        
    def update(self, amount):
        self.stock = amount

    def value(self):
        value = self.price * self.stock
        return value

    def total_value(self):
        total_value = 0
        total_value += self.price * self.stock
        return total_value

products = []

#laod products

def load_products():
    products.clear()
    with open("products.txt", "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")
            products.append(Products(parts[0],int(parts[1]),int(parts[2])))
        return products

# save products
def save_products():
    with open("products.txt", "w") as file:
        for product in products:
            file.write(f"{product.name}, {product.stock}, {product.price}\n")

#menu

def menu():
    print("===== INVENTORY SYSTEM =====")
    print("1. Add product")
    print("2. View products")
    print("3. Search product")
    print("4. Update stock")
    print("5. Restock product")
    print("6. Sell product")
    print("7. Product value")
    print("8. Total inventory value")
    print("9. Exit")

#1. Add product
def add_products():
    name = input("input name: ")
    stock = int(input("input stock: "))
    price = int(input("input price: "))
    products.append(Products(name,int(stock),int(price)))
    save_products()
    print(f"{name} is added to products.")

#2. View products

def display_products():
    load_products()
    for product in products:
        product.display()
        print("------------------------")
        
    
#3. Search product

def Search_products():
    load_products()
    with open("products.txt", "r") as file:
        product_name = input("Input name: ")
        found = False
        for line in file:
            line = line.strip()
            parts = line.split(",")
        if product_name == parts[0]:
            found = True
            print("found entry: ", product_name)
        if not found:
            print("product not found")

#4. Update stock

def update_products():
        load_products()
        product_name = input("Input name: ")
        amount = int(input("Input amount: "))
        found = False
        for product in products:
            if product.name == product_name:
                found = True
                product.update(amount)
                print(f"{product_name}is updated with {amount} items.")
            if not found:
                print("product not found")
            else:
                save_products()
        
#5. Restock product

def restock_products():
        load_products()
        product_name = input("Input name: ")
        amount = int(input("Input amount: "))
        found = False
        for product in products:
            if product.name == product_name:
                found = True
                product.restock(amount)
                print(f"{product_name}is restocked with {amount} items.")
            if not found:
                print("product not found")
            else:
                save_products()
#6. Sell product

def sell_products():
        load_products()
        product_name = input("Input name: ")
        amount = int(input("Input amount: "))
        found = False
        for product in products:
            if product.name == product_name:
                found = True
                product.sell(amount)
                print(f"{product_name}is sold {amount} items.")
            if not found:
                print("product not found")
            else:
                save_products()

#7. Product value

def value_products():
        load_products()
        product_name = input("Input name: ")
        found = False
        for product in products:
            if product.name == product_name:
                found = True
                print(f"{product_name} value: {product.value()}")
            if not found:
                print("product not found")
            else:
                save_products()
#8. Total inventory value

def total_value_products():
    load_products()
    for product in products:
        print(f"total value: {product.total_value()}")
    save_products()