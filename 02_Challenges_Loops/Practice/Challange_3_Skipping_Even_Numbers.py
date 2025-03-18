#-----------------------------------------------------------------------------
# Name:   Challenge 3:Skipping Even Numbers (For Loop + Continue)
# Purpose:  a program that prints numbers from `1` to`10`,
# but skips even numbers using the`continue`statement.
# Author:      Mrs.NN
# Created:     18-March-2025
# Updated:     18-March-2025
#-----------------------------------------------------------------------------
# Loop through numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0: # Check if the number is even
        continue # Skip even numbers
    print(num)
    # Print only odd numbers