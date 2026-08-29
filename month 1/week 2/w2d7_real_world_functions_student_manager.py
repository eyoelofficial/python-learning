def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = [part.strip() for part in line.split(",")]
                if len(parts) >= 2:
                    students.append({"name": parts[0], "age": parts[1]})
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['age']}\n")


def show_menu():
    print("1. add student")
    print("2. remove student")
    print("3. view data")
    print("4. exit")


def add_student(name, age):
    students = load_students()
    students.append({"name": name, "age": age})
    save_students(students)
    print(f"{name} is added.")
def remove_student(name):
    students = load_students()
    for student in students:
        if student["name"] == name:
            students.remove(student)
            save_students(students)
            print(f"{name} is removed.")
            return
    print(f"{name} not found.")


def view_data():
    students = load_students()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}")

while True:
    show_menu()
    choice = input("choose 1/2/3/4: ")
    if choice == "1":
        name = input(" enter name you want to add: ")
        age = input(" enter age you want to add: ")
        add_student(name, age)
    elif choice == "2":
        name = input(" enter name you want to remove: ")
        remove_student(name)
    elif choice == "3":
        view_data()
    elif choice == "4":
        break
    else:
        print("invalid,")
        continue