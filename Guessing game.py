import random

print("-Number Guessing Game-")

#randint means random integer
number=random.randint(1, 9)
chances=0

print("Guess a Number Between 1 and 9:")

while chances<5:
    #we put int because we know the player has to enter an integer and it would be an error if they put anything else
    guess=int(input("What Number did you guess?"))
    if guess==number:
        print("Too sad... you guessed CORRECT")
        break
    elif guess<number:
        print("Too low, guess higher than", guess)
    else:
        print("Too high, guess lower than", guess)

chances += 1

if not chances<5:
    print("Congradulations!! you lost, the number was", number)
