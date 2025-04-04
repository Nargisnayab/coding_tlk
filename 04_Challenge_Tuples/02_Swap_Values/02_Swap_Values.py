# Program Name: Swap Values Using Tuples
# Purpose: Swaps two user-provided values using tuple unpacking.
# Creator: NN
# Date: March 2025
#_____________________________________________________________________
# Taking input from the user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Storing values in a tuple
numbers = (num1, num2)
print(numbers)

# Swapping values using tuple unpacking
num1, num2 = num2, num1
numbers = (numbers[5],numbers[0])
# Printing swapped values
print(numbers)
print(numbers[1])
