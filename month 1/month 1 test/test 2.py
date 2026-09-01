
def inventory_report(products):
    total_number_of_products= len(products)
    print(f"total products: {total_number_of_products}")
    total_stock=sum(product["stock"] for product in products)
    print(f"total stock: {total_stock}")
    highest_price_product = max(products, key=lambda product: product["stock"])
    print(f"Highest stock: {highest_price_product["name"]}")
    lowest_price_product = min(products, key=lambda product: product["stock"])
    print(f"lowest stock: {lowest_price_product["name"]}")
    print(" ")
    has_low_stock = list(filter(lambda product: product["stock"]<25, products))
    has_low_stock_name = list(map(lambda product: product["name"], has_low_stock ))
    for product in has_low_stock_name:
        print(product)
    print(" ")
    heighest_price_product = list(filter(lambda product: product["price"]>800, products))
    heighest_price_product_name = list(map(lambda product: product["name"], heighest_price_product ))
    for product in heighest_price_product_name:
        print(product)
print("==================inventory report==================")
inventory_report(products)
