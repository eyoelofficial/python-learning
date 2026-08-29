while True:
    print("1. Write today's journal")
    print("2. Read old journal")
    print("3. Exit")
    choose = input("choose 1/2/3: ")
    if choose == "1":
        with open("journal.txt", "a") as file:
            while True:
                close = input("close journal? (y/n): ")
                if close == "n":
                    entery = input("journal entry: ")
                    file.write(entery + "\n")
                elif close == "y":
                    print("journal closed")
                    break
    elif choose == "2":
        with open("journal.txt", "r") as file:
            content = file.read()
            print(content)
    elif choose == "3":
        print("Exiting...")
        break
        