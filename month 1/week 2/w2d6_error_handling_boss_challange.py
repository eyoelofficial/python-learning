while True:
    # menu
    print("1. Add journal entry")
    print("2. View journal")
    print("3. Search journal")
    print("4. Exit")
    menu_choice = input("Choose an option 1/2/3/4: ")
    # adding journal entry
    if menu_choice == "1":
        with open("journal.txt", "a") as file:
            while True:
                try:
                    date = int(input("enter date: "))
                    title = input("enter journal title: ")
                    entry = input("enter journal entry: ")
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
                else:
                    file.write(f"{date}\n: {title}\n: {entry}\n")
                    close = input("continue journal? (y/n): ")
                finally:
                    print("Journal entry added successfully.")
                    if close == "y":
                        continue
                    elif close == "n":
                        break
    # viewing journal
    elif menu_choice == "2":
        with open("journal.txt", "r") as file:
            print(file.read())
    # searching journal
    elif menu_choice == "3":
        search_term = input("Enter search term: ")
        with open("journal.txt", "r") as file:
            try:
                entries = file.readlines()
                found = False
                for i in range(len(entries)):
                    if search_term in entries[i]:
                        found = True
                        print("found entry: ", entries[i])
                if not found:
                        print("No entries found with the search term.")
            except Exception as e:
                print(f"An error occurred: {e}")
            else:
                print("Search completed successfully.")
            finally:
                print("Search operation finished.")
    # exiting program
    elif menu_choice == "4":
        print("exitting....")
        break