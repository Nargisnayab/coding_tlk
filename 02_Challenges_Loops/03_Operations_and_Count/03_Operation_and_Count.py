# Program Name:  Tuple Operations & Count
# Purpose:  Count occurrences of a user-specified fruit in a tuple.
# Creator: NN
# Date: March 28, 2025

# Creating a tuple with repeated fruit names
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Asking the user to enter a fruit name
fruit_name = input("Enter a fruit name: ").strip().lower()

# Counting the occurrences of the fruit in the tuple
count = fruits.count(fruit_name)

# Displaying the result
print(f"'{fruit_name}' appears {count} times in the tuple.")
