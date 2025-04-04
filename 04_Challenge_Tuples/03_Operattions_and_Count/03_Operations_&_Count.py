# Program Name: Tuples Operation & Count
# Purpose: tuple with repeated values,
# Creator: NN
# Date: March 2025
#____________________________________________________________
#  Create a tuple with repeated values
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

# Count occurrences of the fruit in the tuple
count = fruits.count(fruit_name)

#  Print the result
print(f"'{fruit_name}' appears {count} times in the tuple.")


