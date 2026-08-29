product_names = ["burger", "tacos", "chicken", "pizza", "cola"]
product_price = [600, 800, 850, 400, 60]
product_stock = [100, 20, 50, 10, 600]

product_tuples = list(zip(product_names, product_price, product_stock))
for name,price,stock in product_tuples:
    print(f"{name} | {price} | {stock}")
for product in product_tuples:
    print(f"{product[0]} | {product[1]} | {product[2]}")