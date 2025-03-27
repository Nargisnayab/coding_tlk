#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Nargis
# Created:     27-feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
# Loop through numbers from 1 to 10
 for num in range(1, 11):
    if num % 2 == 0: # Check if the number is even
        continue # Skip even numbers
    print(num)
    # Print only odd numbers