while True:
    def show_menu():
        print("1. Hello")
        print("2. Bye")
    show_menu()
    choice = input(": ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        break