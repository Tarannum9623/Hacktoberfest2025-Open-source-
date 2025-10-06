import random
from replit import clear

clear()
EASY_TURNS = 10
HARD_TURNS = 5


print("Welcome to Number Guessing Game!\nI am Guessing a number between 1-100. ")
i = random.randint(1,100)
# print(i)
level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
chance = 0
if level == 'hard':
    chance = 5
else:
    chance = 10
eog = False
while not eog and chance !=0:
    ans = int(input("Make a Guess : "))
    chance-=1
    if ans > i:
        print("Too high.")
    elif ans < i:
        print("Too low.")
    else:
        print(f"You got it! The answer was {i}")
        eog = True

    if not eog and chance>0:
        print("Guess again.")
        print(f"You have {chance} attempts remaining to guess the number.")
    elif not eog:
        print("You've run out of guesses, you lose.")
        eog = True
