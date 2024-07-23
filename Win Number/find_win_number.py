import random

control = True
rand = random.randint(1,100)
while control:
    number = int(input("Guess the Number : "))
    if number > rand:
        print("to heigh .")
    elif number < rand:
        print("to low")
    elif number == rand:
        print("good guessing")
        control = False
