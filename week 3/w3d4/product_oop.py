from products_oop_list import Product, menu, View_inventory,update_stock,seach

while True:
    menu()
    choice = input("choose 1/2/3/4: ")
    if choice == "1":
        View_inventory()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        seach()
    elif choice == "4":
        print("exitting...")
        break