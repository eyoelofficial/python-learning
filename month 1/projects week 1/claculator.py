print("------------------Calculator------------------")
while True:
    op = str(input(" choose your mathimatical opporation. if addition(+), if substraction(-) if multiplication(*)and if divition(/) and if u eant to exit/quit(q)"))
    if op == "q":
        print("------------------Calculator------------------")
        break
    o1 = float(input('1st number: '))
    o2 = float(input('2nd number: '))
    if op == "+":
        answer = o1 + o2
        print(answer)
    elif op == "-":
        answer = o1 - o2
        print(answer)
    elif op == "*":
        answer = o1 * o2
        print(answer)
    elif op == "/":
        if o2 == 0:
            print("invalid input: no number can be devided by 0")
            break
        answer = o1 / o2
        print(answer)
    