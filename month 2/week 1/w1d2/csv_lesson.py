import csv
with open("products.csv", "r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        name=row[0]
        price=int(row[1])
        stock=int(row[2])
        print(name,price,stock)