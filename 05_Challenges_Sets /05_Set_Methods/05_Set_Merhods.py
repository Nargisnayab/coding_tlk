# Program Name:        Set Methods
# Purpose:        Demonstrate various set methods
# creator:            NN
# Date:       3-Apr-2025
#_____________________________________________________________________
#  Create a set `data
data = {10, 20, 30, 40, 50}
# Copying the set
data_copy = data. copy()
print("Copy",data_copy)

# Using pop() to remove a random element and print the set
data.pop()
print("After pop" ,data)

# Using clear to empty the set and print it
data.clear()
print("After clear" , data)