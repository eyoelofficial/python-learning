from boss_list_oop import Products, menu, add_products, display_products, Search_products, update_products, restock_products, sell_products, value_products, total_value_products
while True:
    menu()
    choice = input("1/2/3/4/5/6/7/8/9: ")
    if choice == "1":
        add_products()
    elif choice == "2":
        display_products()
    elif choice == "3":
        Search_products()
    elif choice == "4":
        update_products()
    elif choice == "6":
        sell_products()
    elif choice == "5":
        restock_products()
    elif choice == "7":
        value_products()
    elif choice == "8":
        total_value_products()
    elif choice == "9":
        break
