from w3d6_oop_list import Products,menu_products,view_products, restock_products,sell_products,value_products
while True:
    menu_products()
    choice = input("choose 1/2/3/4/5: ")
    if choice =="1":
        view_products()
    elif choice == "2":
        restock_products()
    elif choice == "3":
        sell_products()
    elif choice == "4":
        value_products()
    elif choice == "5":
        break