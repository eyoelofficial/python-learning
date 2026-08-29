from products_oop_list_v2 import Product, menu, update_stock,search,View_inventory,Restock_products, sell_products,inventory_value_product,total_inventory_value_product

while True:
    menu()
    choice = input("choose 1/2/3/4/5/6/7/8: ")
    if choice == "1":
        View_inventory()
    elif choice == "2":
        search()
    elif choice == "3":
        update_stock()
    elif choice == "4":
        Restock_products()
    elif choice == "5":
        sell_products()
    elif choice == "6":
        inventory_value_product()
    elif choice == "7":
        total_inventory_value_product()
    elif choice == "8":
        print("exitting...")
        break