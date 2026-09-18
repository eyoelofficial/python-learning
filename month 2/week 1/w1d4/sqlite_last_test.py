import sqlite3
connect= sqlite3.connect("products_2.db")
cursor=connect.cursor()
cursor.execute("""
    SELECT * FROM product
    WHERE name = ?
    AND price = ?
    AND stock = ?
""",('rice',120, 30))
existing = cursor.fetchone()
if existing:
    print("existes")
else:
    cursor.execute("""
    INSERT INTO product (name,price,stock)
    VALUES ('rice',120,50)
    """)
    connect.commit()
    print("added")

cursor.execute("SELECT * FROM product")
products = cursor.fetchall()
for product in products:
    print(f"{product[0]}|{product[1]}|{product[2]}")
