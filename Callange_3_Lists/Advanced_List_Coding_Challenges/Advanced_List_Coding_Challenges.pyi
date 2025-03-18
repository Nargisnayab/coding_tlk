#-----------------------------------------------------------------------------
# Name:        Challenge 1: Nested List Operations
# Purpose:     Work with a nested list to access, modify, and manipulate data
# Author:      Mrs. NN
# Created:     21-March-2025
# Updated:     21-March-2025
#------------------------------------------------------------------------

# Creating the nested list
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]

# Updating Bob's information
students[1][1] = 23  # Change age to 23
students[1][2] = 'Mathematics'  # Change major

# Printing the updated list
print(students)

# Finding the student studying Biology
for student in students:
    if student[2] == 'Biology':
        print(student[0])  # Print name of student studying Biology