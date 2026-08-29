print("------------------todo list------------------")
tasks = []
while True:
    print("start y/n")
    a = input(": ")
    if a == "y":
        print(" menu")
        print("1. add task")
        print("2. remove task")
        print("3. view task")
        print("4. exit")
        b = input(": ")
        if b == "1":
            while True:
                c = input("list a task if done(0): ")
                tasks.append(c)
                if c == "0":
                    break
        if b == "2":
            while True:
                c = input("list the task if done(0): ")
                tasks.remove(c)
                if c == "0":
                    break
        if b == "3":
            print(tasks)
        if b == "4":
            break
    else:
        break
print("------------------todo list------------------")