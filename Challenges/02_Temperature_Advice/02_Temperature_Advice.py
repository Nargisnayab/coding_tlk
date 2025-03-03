#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Nargis
# Created:     27-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
temperature = int(input("Enter the temperature (°C) "))
if  temperature   > 10:
  print ("It's cold outside .Wear a jacket")
elif  10 <= temperature <= 25:
  print ("It's a nice day. Wear short-sleeves!")
else:
     print ("It's hot outside.Stay cool!")


