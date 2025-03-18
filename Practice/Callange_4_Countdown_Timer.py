## 🏆 Challenge 4: Countdown Timer (While Loop + Break)
#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Nargis
# Created:     27-feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
# Initialize countdown starting at 10
count = 10

# Loop while count is greater than 0
while count > 0:
    print(count)
    # Print the current countdown number
    user_input = input('Enter "stop" to cancel or press Enter: ') # Ask user for input

    if user_input.lower() == "stop": # Check if user entered "stop"
        print("Countdown stopped!")
        break # Exit the loop

    count -= 1 # Decrease the countdown number

# If the loop ends normally, print "Countdown finished!"
if count == 0:
    print("Countdown finished!")