import random
number = random.randint(0, 10000)

while True:
    guess = int(input("Guess a number between 1 and 10000: "))
    if guess < number:
        print("Increase!!!")
    elif guess > number:
        print("Decrease!!!")
    else:
        print("Congrats!!!")
        break