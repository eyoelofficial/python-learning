import random, math, time
from datetime import datetime
def Utility():
    print("===== Utility Toolbox =====")
    print("1. Random number")
    print("2. Random food")
    print("3. Square root")
    print("4. Show Pi")
    print("5. Show current date & time")
    print("6. Countdown")
    print("7. Exit")
def Random_number(min,max):
    Random_number_answer = random.randint(min, max)
    return Random_number_answer
def Random_food():
    food = ["Pizza","Burger","Rice","Pasta","Chicken"]
    Random_food_answer = random.choice(food)
    return Random_food_answer
def Square_root(number):
    Square_root_answer = math.sqrt(number)
    return Square_root_answer
def Show_Pi():
    Show_Pi_answer = math.pi
    return Show_Pi_answer
def Show_current_date_and_time():
    Show_current_date_and_time_answer = datetime.now()
    return Show_current_date_and_time_answer
def Countdown(number):
    Countdown_answer = time.sleep(number)
    return Countdown_answer