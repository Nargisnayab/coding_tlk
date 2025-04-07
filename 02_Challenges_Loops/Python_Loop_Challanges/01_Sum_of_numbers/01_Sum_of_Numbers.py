# -----------------------------------------------------------------------------
# Name:         Introduction to Loops in Python
# Purpose:     A `for` loop is used when you want to iterate over a sequence (like a list, tuple, string, or range).
# Author:      Mrs.NN
# Created       18-March-2025
# Update        18-March-2025
#-----------------------------------------------------------------------------
# write a program that asks the user for a number `n` a `for` loop.
#  Enter number: 5
n = int(input("Enter a number: "))
sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i
print("Sum =", sum_numbers)