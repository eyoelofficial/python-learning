try:
    age = int(input("age: "))
except ValueError:
    print("Invalid input")
else:
    print("Next year, you will be ", age + 1)