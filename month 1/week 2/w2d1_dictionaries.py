book = {"title": "the book of the dead", "author":"elberto", "price":120, "page": 352}
while True:
    print("start y/n")
    answer = input(": ")
    if answer == "y":
        print(" menu")
        print("1. change ")
        print("2. remove ")
        print("3. view ")
        print("4. exit")
        menu = input(": ")
        if menu == "1":
            while True:
                changes = input("enter the key you want to add (0 to finish): ")
                if changes == "0":
                    break
                book[changes] = input(f"enter new value for {changes}: ")
        if menu == "2":
            while True:
                changes = input("enter the key you want to remove (0 to finish): ")
                if changes == "0":
                    break
                del book[changes]
        if menu == "3":
            print(book)
        if menu == "4":
            break
    else:
        break