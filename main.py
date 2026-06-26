inventory = []

while True:
    print("\n1. add item")
    print("2. show item")
    print("3. remove items")
    print("4. exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("item name: ")
        inventory.append(item)
        print("added item successfully")
    elif choice == '2':
        print("items in inventory: ", inventory)
    elif choice == '3':
        item = input("item to remove: ")
        if item in inventory:
            inventory.remove(item)
            print("removed item successfully")
        else:
            print("item not found in inventory")
    elif choice == '4':
        break