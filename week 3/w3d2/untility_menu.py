from utillity_box import Utility,Random_number,Random_food,Square_root,Show_Pi,Show_current_date_and_time,Countdown
while True:
    Utility()
    choice = input("choice: ")
    if choice == "1":
        min = int(input("enter minimum number: "))
        max = int(input("enter maximum number: "))
        print(Random_number(min,max))
    elif choice == "2":
        print(Random_food())
    elif choice == "3":
        number = int(input("enter the number: "))
        print(Square_root(number))
    elif choice == "4":
        print(Show_Pi())
    elif choice == "5":
        print(Show_current_date_and_time())
    elif choice == "6":
        number = int(input("enter the number: "))
        print(Countdown(number))
    elif choice == "7":
        break