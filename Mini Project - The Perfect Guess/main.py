# A program which generates a random number and asks user to guess it.

# If user's guess is higher than the generated number, the program displays "Lower".
# If user's guess is lower than the generated number, the program displays "Higher".

# Lower the number of guesses, better the score. Program displays number of guesses user made before guessing the generated number.

from random import randint  # import random
n = randint(1, 100)         # n = random.randint(1, 100)

a = -1

guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if a>n:
        print("Lower")
    else:
        print("Higher")

print(f"You have guessed the number ({n}) correctly. Number of guesses: {guesses}")