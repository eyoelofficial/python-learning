while True:
    print("1. Add journal entry")
    print("2. View journal")
    print("3. Search journal")
    print("4. Exit")
    menu_choice = input("Choose an option 1/2/3/4: ")
    if menu_choice == "1":
        with open("journal.txt", "a") as file:
            while True:
                date = input("enter date: ")
                title = input("enter journal title: ")
                entry = input("enter journal entry: ")
                file.write(f"{date}\n: {title}\n: {entry}\n")
                close = input("continue journal? (y/n): ")
                if close == "y":
                    continue
                elif close == "n":
                    break
    elif menu_choice == "2":
        with open("journal.txt", "r") as file:
            print(file.read())
    elif menu_choice == "3":
        search_term = input("Enter search term: ")
        with open("journal.txt", "r") as file:
            entries = file.readlines()
            for i in range(len(entries)):
                if search_term in entries[i]:
                    print("found entry: ", entries[i])
    elif menu_choice == "4":
        print("exitting....")
        break