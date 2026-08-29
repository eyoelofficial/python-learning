while True:
    def show_menu():
        print("1. Hello")
        print("2. Bye")
    def say_hello():
        print("Hello, world!")
    show_menu()
    choice = input(": ")
    if choice == "1":
        say_hello()
    elif choice == "2":
        break