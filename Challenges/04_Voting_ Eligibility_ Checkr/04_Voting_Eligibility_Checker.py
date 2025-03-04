-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Nargis
# Created:     27-feb-2025
# Updated:     27-Feb-2025
#--------------------------------------------------------------------------
# Ask the user to enter their age. Store the age in a variable.
age = int(input("Enter your age: "))
If the age is 18 or older, print: `"You are eligible to vote!"`
#If the age is 18 or older, print: `"You are eligible to vote!"`
if age >= 18:
    print("You are eligible to vote!")
# If the age is under 18, print: `"Sorry, you are not eligible to vote yet."`
else:
    print("Sorry, you are not eligible to vote yet.")