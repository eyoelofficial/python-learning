class Products:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")

    def restock(self,amount):
        self.stock += amount

    def sell(self, amount):
        self.stock -= amount

    def value(self):
        Value = self.price * self.stock
        return Value

burger = Products("burger",350,30)
pizza = Products("pizza",450,15)
cola = Products("cola",60,50)

products = [burger,pizza, cola]

def menu_products():
    print("menu")
    print("1. display products")
    print("2. restock products")
    print("3. sell products")
    print("4. value products")

def view_products():
    burger.display()
    pizza.display()
    cola.display()    

def restock_products():
    name = str(input("name of the restocked product: "))
    amount = int(input("enter amount: "))
    found = False
    for product in products:
        if product.name == name:
            product.restock(amount)
            print("restocked")
            found = True
    if not found:
        print("couldn't find the product")

def sell_products():
    name = str(input("name of the sold product: "))
    amount = int(input("enter amount: "))
    found = False
    for product in products:
        if product.name == name:
            product.sell(amount)
            print("sold")
            found = True
        if not found:
            print("couldn't find the product")
def value_products():
    total = 0
    try:
        for product in products:
            total += int(product.value())
            print(total)
    except ValueError:
        print(" product not found")