## 🏆 Challenge 2: Guess the Number (While Loop)
#-----------------------------------------------------------------------------
# Name:   Challenge 2: Guess the Number (While Loop)
# Purpose:  `1` and `10` and keeps asking the user to guess it using
# a `while` loop **until they guess correctly
#
# Author:      Mrs.NN
# Created:     18- March-2025
# Updated:     18-March-2025
#-----------------------------------------------------------------------------
# generates a random number between `1` and `10`
import random # Import the random module
# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess the number
guess = 0 # Initialize variable

# Keep looping until the user guesses correctly
while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
# Guess the number: 4
if guess < secret_number:
    print("Too low, try again!")
# Wrong, try again!
elif guess < secret_number:
    print(" Too high, try again!")
else:
# User guessed correctly
     print("Correct! 🎉")
