#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Nargis
# Created:     27-feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# Ask the user to enter the current temperature (in Celsius).Store the temperature in a variable.
temperature = int(input("Enter the temperature (°C) "))

#If the temperature is below 10°C, print: `"It's cold outside. Wear a jacket!"`
if  temperature   > 10:
  print ("It's cold outside .Wear a jacket")

# - If the temperature is between 10°C and 25°C, print: `"It's a nice day. Wear short-sleeves!"`
elif  10 <= temperature <= 25:
  print ("It's a nice day. Wear short-sleeves!")

# If the temperature is above 25°C, print: `"It's hot outside. Stay cool!"
else:
     print ("It's hot outside.Stay cool!")


