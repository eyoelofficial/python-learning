import csv
with open("products.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        inventory_value=int(row["price"])*int(row["stock"])
        print(f"{row["name"]} | {int(row["price"])} | {int(row["stock"])} | {inventory_value}")