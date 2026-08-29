def create_profile(name, age, job):
    return f"Name: {name}, Age: {age}, Job: {job}"
name = input("Enter your name: ")
age = input("Enter your age: ")
job = input("Enter your job: ")
profile = create_profile(name, age, job)
print(profile)
