class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock            

    def display(self):
        print(f"Name:  {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print("----------------------")

    def update(self,amount):
        self.stock = amount
    
    def Restock(self,amount):
        self.stock += amount
        
    def sell(self,amount):
        self.stock -= amount

    def value(self):
        value_product = self.stock * self.price
        return value_product

    def total_value(self):
            value_burger = burger.stock * burger.price
            value_pizza = pizza.stock * pizza.price
            value_cola = cola.stock * cola.price
            total_inventory_value_products = value_cola + value_pizza + value_burger
            return total_inventory_value_products
            
burger = Product("burger",120,10)
pizza = Product("pizza",220,15)
cola = Product("cola",60,200)

products = [burger,pizza,cola]
        
#menu

def menu():
        print("===menu===")
        print("1. View inventory")
        print("2. Search product")
        print("3. Update stock")
        print("4. Restock product")
        print("5. Sell product")
        print("6. inventory value")
        print("7. total inventory value")
        print("8. exit")

#1. View inventor

def View_inventory():
    print("-----view inventory-----")
    burger.display()
    pizza.display()
    cola.display()

#2. Search product

def search():
    print("-----search product-----")
    x = input("input product name: ")
    try:
        for search in products:
            if search.name == x:
                search.display()
                print("test")
    except ValueError:
        print("error")

#3. Update stock

def update_stock():
    print("-----update product stock-----")
    product_name = str(input("input product name: "))
    amount = int(input("input new stock: "))
    try:
        for product in products:
            if product.name == product_name:
                product.update(amount)
                print(f"{product_name} is updated.")
    except ValueError:
        print(" product not found")

#4. Restock product

def Restock_products():
    print("-----Restock product-----")
    product_name = str(input("input product name: "))
    amount = int(input("input new stock: "))
    try:
        for product in products:
            if product.name == product_name:
                product.Restock(amount)
                print(f"{product_name} is updated.")
    except ValueError:
        print(" product not found")

#5. Sell product

def sell_products():
    print("-----sell product-----")
    product_name = str(input("input product name: "))
    amount = int(input("input new stock: "))
    try:
        for product in products:
            if product.name == product_name:
                product.sell(amount)
                print(f"{product_name} is updated.")
    except ValueError:
        print(" product not found")

#6. inventory value

def inventory_value_product():
    print("-----inventory value-----")
    product_name = str(input("input product name: "))
    try:
        for product in products:
            if product.name == product_name:
                print(f"{product_name}: = {product.value()}")              
    except ValueError:
        print(" product not found")

#7. total inventory value

def total_inventory_value_product():
    print("-----inventory value-----")
    total = 0
    try:
        for product in products:
            inventory_value_product = total + int(product.total_value())
            print(inventory_value_product)
    except ValueError:
        print(" product not found")