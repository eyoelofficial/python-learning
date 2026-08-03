from inventory_list import products, menu,View_inventory,Search_product,Change_stock,total_inventory_value
while True:
    menu()
    choice = input("choose 1/2/3/4/5: ")
    if choice == "1":
        View_inventory()
    elif choice == "2":
        search = input("Search: ")
        Search_product(search)
    elif choice == "3":
        product_name = input("enter product name: ")
        new_stock = int(input("update stock: "))
        Change_stock(product_name,new_stock)
    elif choice == "4":
        total_inventory_value()
    elif choice == "5":
        break