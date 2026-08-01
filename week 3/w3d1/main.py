from maths import add,sub,div,mult,power
try:
    while True:
        print("calculator v2")
        print("1. addition")
        print("2. substration")
        print("3. multipliction")
        print("4. divition")
        print("5. power")
        print("6. exit")
        choice = input("choose (1/2/3/4/5/6):")
        a = float(input("first number: "))
        b = float(input("seconed number: "))
        if choice == "1":
            print(add(a,b))
        elif choice == "2":
            print(sub(a,b))
        elif choice == "3":
            print(mult(a,b))
        elif choice == "4":
            print(div(a,b))
        elif choice == "5":
            print(power(a,b))
        if choice == "6":
            print("exitting...")
            break
except ValueError:
    print(" an error has occuered, please review your code :)")

