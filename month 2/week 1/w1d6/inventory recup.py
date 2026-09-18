import sqlite3
connect = sqlite3.connect("inventorSy_recup.db")
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY,
    category TEXT,
    name TEXT UNIQUE,
    price INTEGER,
    stock INTEGER
    )""")
connect.commit()
def menu():
    print("1. Add products\n" \
        "2. Show products\n" \
        "3. Search Product\n" \
        "4. Update stock\n" \
        "5. Delete product" )

def add_products():
    name = input("Product Name: ")
    category_choice = input("choose category:\n" \
                            "1. liquids\n" \
                            "2. refregatable foods\n" \
                            "3. vagitables/fruits\n" \
                            "4. long shalf time\n" \
                            "5. non food items\n")
    if category_choice == "1":
            category = "liquids"
    elif category_choice == "2":
            category = "refregatable foods"
    elif category_choice == "3":
            category = "vagitables/fruits"
    elif category_choice == "4":
            category = "long shalf time"
    elif category_choice == "5":
            category = "non food items"
    else:
        category = "unknown"
    price = int(input("Product price: "))
    stock = int(input("Product stock: "))
    cursor.execute("""
        INSERT INTO inventory(name, category, price, stock)
        VALUES (?, ?, ?, ?)
        """,(name, category, price, stock,))
    connect.commit()
    product = find_product(name)
    print("your product is added:")
    id, category, name ,price ,stock = product
    print(f"{id} | {category} | {name} | {price} | {stock}")
    
def Show_products():
        cursor.execute("SELECT * FROM inventory")
        products = cursor.fetchall()
        for product in products:
             print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]} | {product[4]} |")

def find_product(name):
    cursor.execute("""
        SELECT * FROM inventory
        WHERE name = ?""",(name,))
    product = cursor.fetchone()
    return product

def search_product():
    name = input("Name: ")
    product = find_product(name)
    if product:
        print("your product is Found:")
        id, category, name ,price ,stock = product
        print(f"{id} | {category} | {name} | {price} | {stock}")
    else:
          print(f"Product was not found")

def Update_stock():
    name = input("Name: ")
    product = find_product(name)
    if product:
        print("your product is found:")
        id, category, name ,price ,stock = product
        print(f"{id} | {category} | {name} | {price} | {stock}")
        stock = int(input("Product stock: "))
        cursor.execute("""
        UPDATE inventory
        SET stock = ?
        WHERE name = ?
        """,(stock, name))
        connect.commit()
        product = find_product(name)
        id, category, name ,price ,stock = product
        print(f"{id} | {category} | {name} | {price} | {stock}")
    else:
        print(f"Product was not found")

def Delete_product():
    name = input("Name: ")
    product = find_product(name)
    if product:
        id, category, name ,price ,stock = product
        print(f"{id} | {category} | {name} | {price} | {stock}")
        cursor.execute("""
            DELETE FROM inventory
            WHERE name = ?""",(name,))
        print(f"{name} was deleted.")
        connect.commit()
    else:
        print(f"Product wasn't found.")

def exit_():
    print("thanks for using.\nexitting...".title())

while True:
    print("========Inventory========")
    menu()
    choice = input("choose(1/2/3/4/5 and press any button to exit.): ")
    if choice == "1":
        add_products()
    elif choice == "2":
        Show_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        Update_stock()
    elif choice == "5":
        Delete_product()
    else:
        exit_()
        print("========Inventory========")
        break