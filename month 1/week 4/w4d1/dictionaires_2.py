product = {
    "name": "burger",
    "price": 300,
    "stock": 21
}
product['category'] = "food"
print(product)
product["price"] = 350
print(product)
product["discount"] = 20
print(product)
if "discount" in product:
    print(product["discount"])
print(product.get("discount"))
del product["category"]
print(product.get("stock", 0))
print("1")
print(product.get())
