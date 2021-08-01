# import the random module

import random


guess = int(input("Enter your guess between 1 and 100: "))

# code to keep the game running until the user wins

number = random.randrange(1, 100)
while guess != number:
    if guess < number:
        print("Too low!")
        guess = int(input("Enter your guess: "))
    else:
        print("Too high!")
        guess = int(input("Enter your guess: "))
    
# the code for when the user wins


print("You win!")


