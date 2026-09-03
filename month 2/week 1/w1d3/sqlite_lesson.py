import sqlite3
connect=sqlite3.connect("products.db")
cursor = connect.cursor()
print("connected!")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product(
    name TEXT,
    price INTEGER,
    stock INTEGER
)""")
connect.commit()
print("saved!")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
table = cursor.fetchall()
print(table)
cursor.execute(
    """INSERT INTO product (name, price, stock)
    VALUES ('chicken',900,10)
    """
)
cursor.execute("""
    INSERT INTO product (name, price, stock)
    VALUES ('beef', 100, 20)
""")
cursor.execute("""
    INSERT INTO product (name, price, stock)
    VALUES ('milk', 80, 15)
""")
cursor.execute("""
    INSERT INTO product (name, price, stock)
    VALUES ('bread', 1200, 5)
""")
connect.commit()
print("committed")
cursor.execute("SELECT * FROM product")
product = cursor.fetchone()
print(product)
print(" ")
cursor.execute("""
    SELECT * FROM product
    WHERE name = 'chicken'
""")
products = cursor.fetchall()
print(products)
print(" ")
cursor.execute("""
    SELECT * FROM product
    WHERE stock < 10
""")
products = cursor.fetchall()
print(products)
print(" ")
cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
print(products)
limit = 15
print("4")
cursor.execute("""
    SELECT * FROM product
    WHERE stock <= ?
""",(limit,))
products = cursor.fetchall()
print(products)

print("3")
cursor.execute(
    """
    UPDATE product
    SET stock = 3
    WHERE name = 'bread'
"""
)
connect.commit()
cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
print(products)
print("2")

cursor.execute("""
    DELETE FROM product
    WHERE name = 'bread'
""")
connect.commit()
cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
print(products)

cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
print(products)
print("1")

print("done?")