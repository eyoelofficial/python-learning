import csv
low_stock=[]
with open("new_products.csv","r") as file:
    reader=csv.DictReader(file)
    for product in reader:
        if int(product["stock"])<=20:
            low_stock.append(product)
            
with open("low_stock.csv","w") as file:
    fieldnames=["name","price","stock"]
    writer=csv.DictWriter(file, fieldnames)
    writer.writeheader()
    for product in low_stock:
        writer.writerow(product)
    print("done1")
