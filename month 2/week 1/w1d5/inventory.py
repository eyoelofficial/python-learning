import sqlite3

connect = sqlite3.connect("inventory.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        price INTEGER,
        stock INTEGER
    )
""")

connect.commit()
def menu():
    print(" 1. Add product\n 2. Show products\n 3. Search product\n 4. Update stock\n 5. Delete product\n 6. Exit")

#1

def insert_product():
    name = input("Product name: ")
    price = int(input("Product price: "))
    stock = int(input("Product stock: "))
    cursor.execute("""
        INSERT INTO product (name, price, stock)
        VALUES (?,?,?)
        """,(name, price, stock,))
    connect.commit()
    cursor.execute("""
        SELECT * 
        FROM product
        WHERE name = ?""",(name,))
    products = cursor.fetchone()
    print("your product is added:")
    id,name,price,stock = products
    print(f"{id} | {name} | {price} | {stock}")

#2

def show_products():
    cursor.execute(" SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        print(f"{product[0]}|{product[1]}|{product[2]}|{product[3]}")

#3

def search_product():
    name=input("input name: ")
    cursor.execute("""
            SELECT * 
            FROM product
            WHERE name = ?""",(name,))
    products = cursor.fetchone()
    if products:
        print("here is the product.")
        id,name,price,stock = products
        print(f"{id} | {name} | {price} | {stock}")
    else:
        print(f"{name} wasn't found.")
#4

def update_stock():
    name=input("input name: ")
    cursor.execute("""
                SELECT * 
                FROM product
                WHERE name = ?""",(name,))
    products = cursor.fetchone()
    if products:
        print("before Update")
        id,name,price,stock = products
        print(f"{id} | {name} | {price} | {stock}")    
        stock= int(input("new stock"))
        cursor.execute("""
        UPDATE product
        SET stock = ?
        WHERE name = ?
        """,(stock, name))
        connect.commit()
        cursor.execute("""
            SELECT * FROM product
            WHERE name = ?""",(name,)) 
        products = cursor.fetchone()
        print("After update")
        id,name,price,stock = products
        print(f"{id} | {name} | {price} | {stock}")
    else:
        print(f"not updated, {name} wasn't found.")           
    

#5

def delete_product():
    name=input("input name: ")
    cursor.execute("""
            SELECT * 
            FROM product
            WHERE name = ?""",(name,))
    products = cursor.fetchone()
    if products:
        id,name,price,stock = products
        print(f"{id} | {name} | {price} | {stock}")
        print("deleted")
        cursor.execute("""
                DELETE FROM product
                WHERE name = ?""",(name,))
        connect.commit()
    else:
        print(f"{name} wasn't found.")

    
#6

def exit_():
    print("thanks for using.\nexitting...".title())

while True:
    print("========Inventory========")
    menu()
    choice = input("choose(1/2/3/4/5/6): ")
    if choice == "1":
        insert_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        exit_()
        print("========Inventory========")
        break