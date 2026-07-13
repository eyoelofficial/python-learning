while True:
    def structuer(question, choose_a, choose_b,choose_c, choose_d, answer):
        print(question)
        print(choose_a)
        print(choose_b)
        print(choose_c)
        print(choose_d)
    result = 0
    while structuer("what is 2+2? ", "1", "2", "3", "4", "d"):
    #this like is uttuerly useless#
        print("test")
    #idk why it needs the print command here but what ever#
    choose = str(input("choose: "))
    if choose == "d":
        result += 1
    else:
        break
    print(result)
    break
