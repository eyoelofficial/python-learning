import random
s = random.randint(1, 5)
while True:
    x = float(input("guess then number: "))
    if x >= 6:
        break
    if x == s:
        print("winner")
        break
    else:
        print("try again")
        continue