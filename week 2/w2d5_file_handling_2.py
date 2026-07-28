while True:
    print("------------------------------")
    print("1. Write to file")
    print("2. Read from file")
    print("3. Exit")
    print("4. Delete file")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        file = open("journal.txt", "a")
        entry = input("Enter your journal entry: ")
        file.write(entry + "\n")
        file.close()
        print("Entry added to journal.")
    elif choice == "2":
        file = open("journal.txt", "r")
        content = file.read()
        print("Journal entries:")
        print(content)
        file.close()
    elif choice == "3":
        print("Exiting...")
        print("------------------------------")
        break
    elif choice == "4":
        import os
        if os.path.exists("journal.txt"):
            os.remove("journal.txt")
            print("Journal file deleted.")
        else:
            print("Journal file does not exist.")
    else:
        print("Invalid choice. Please try again.")