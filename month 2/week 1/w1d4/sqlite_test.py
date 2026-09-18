import sqlite3
connect=sqlite3.connect("products.db")
cursor=connect.cursor()
cursor.execute("""
    SELECT * FROM product
    WHERE name = ?
""",('eggs',)
)
existing = cursor.fetchone()
if existing:
    print("existes")

else:
    print("doesn't exit, i will added it.")
    print(" ")
    cursor.execute("""
    INSERT INTO product (name, price, stock)
    VALUE ('eggs',180,200)
    """
)
connect.commit()
cursor.execute(" SELECT * FROM product")
products = cursor.fetchall()
for product in products:
    print(f"{product[0]}|{product[1]}|{product[2]}")