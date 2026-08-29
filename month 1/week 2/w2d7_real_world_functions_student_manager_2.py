def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")
                students.append({"name":parts[0], "age":parts[1], "grade":parts[2]})
            return students
    except FileNotFoundError:
        return students
def show_menu():
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Exit")
def add_student(name, age, grade,):
    students = load_students()
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{grade}\n")
    print(f"Added student: {name}")
def remove_student(name):
    students = load_students()
    for student in students:
        if student["name"] == name:
            students.remove(student)
            with open("students.txt", "w") as file:
                for s in students:
                    file.write(f"{s['name']},{s['age']},{s['grade']}\n")
            print(f"Removed student: {name}")
            return
    print(f"Student not found: {name}")
def view_students():
    students = load_students()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
while True:
    show_menu()
    choice = input("Choose an option 1/2/3/4: ")
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        add_student(name, age, grade)
    elif choice == "2":
        name = input("Enter student name to remove: ")
        remove_student(name)
    elif choice == "3":
        view_students()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose 1/2/3/4.")