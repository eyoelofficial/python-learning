product_name = ["burger", "tacos", "chicken", "pizza", "cola"]
product_price = [600, 800, 850, 400, 60]
product_stock = [100, 20, 50, 10, 600]

product_tuple = list(zip(product_name, product_price, product_stock))
for name,price,stock in product_tuple:
    print(name, price, stock)
has_low_stock = any(product[2]>25 for product in product_tuple)
print(has_low_stock)
has_no_price = all(product[1]>25 for product in product_tuple)
print(has_no_price)