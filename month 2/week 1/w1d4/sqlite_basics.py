import sqlite3
connect=sqlite3.connect("products_2.db")
cursor=connect.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER,
    stock INTEGER
)""")
connect.commit()
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
cursor.execute(" SELECT * FROM product")
products = cursor.fetchall()
print(products)

cursor.execute("""
    SELECT * FROM product
    ORDER BY price DESC;
""")
products = cursor.fetchall()
print(products)

cursor.execute("""
    SELECT name, price, stock
    FROM product
    ORDER BY stock ASC
    LIMIT 2;
""")
products = cursor.fetchall()
for product in products:
    print(f"{product[0]}|{product[1]}|{product[2]}")