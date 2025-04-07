## 🏆 Challenge 4: Countdown Timer (While Loop + Break)
#-----------------------------------------------------------------------------
# Name:        Challenge 4: Countdown Timer (While Loop + Break)
# Purpose:      a program that starts at `10` and counts down to `1`,
# but if the user enters `"stop"`, the countdown should break.
#
# Author:      Mrs.NN
# Created:     18-March-2025
# Updated:     18-March-2025
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
count -= 1 # Decrease the countdown number

# If the loop ends normally, print "Countdown finished!"
if count == 0:
    print("Countdown finished!")