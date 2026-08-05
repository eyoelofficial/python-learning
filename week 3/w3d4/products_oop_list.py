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

burger = Product("burger",120,10)
pizza = Product("pizza",220,15)
cola = Product("cola",60,200)

products = [burger,pizza,cola]

def menu():
        print("===menu===")
        print("1. View inventory")
        print("2. update stock")
        print("3. seach for product")
        print("4. Exit")


def View_inventory():
    burger.display()
    pizza.display()
    cola.display()


def update_stock():
    print("update product stock")
    product_name = str(input("input product name: "))
    new_stock = int(input("input new stock: "))

    try:
        for product in products:
            if product.name == product_name:
                product.stock = new_stock
                print(f"{product_name} is updated.")
    except:
        print(" product not found")
def seach():
    x = input("input product name: ")
    try:
        for search in products:
            if search.name == x:
                search.display()
                print("test")
    except:
        print("error")