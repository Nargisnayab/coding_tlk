
#-----------------------------------------------------------------------------
# Name:        Conditional Statements (conditionalStatements.py)
# Purpose:     To provide information about how conditional statements (if)
#			   work in Python
#
# Author:      Mr. Nargis
# Created:     27-feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------

# Ask the user to enter their score (out of 100) and store it in a variable
myScore =int(input("what's your score out of a 100?: "))

# If the score is greater than or equal to 90, print: `"Grade: A"`
if myScore >= 90:
    print ("Grade: A")

#  If the score is between 80 and 89, print: `"Grade: B"`
elif myScore >= 80 and myScore < 90:
    print ("Grade: B")

# If the score is between 70 and 79, print: `"Grade: C"`
elif myScore >= 70 and myScore < 80:
    print ("Grade: C")

# If the score is between 60 and 69, print: `"Grade: D"`
elif myScore >= 60:
    print ("Grade: D")

#If the score is below 60, print: `"Grade: F"`
else:
    print("Grade:F")
