# Program Name:    Adding and Removing Elements (Using Update and Discard)
# Purpose:       Modify a set efficiently.
# creator:           NN
# Date:       3-Apr-2025
#_____________________________________________________________________
# create a ser litters
letters = {'a', 'b', 'c'}
# Adding multiple elements
letters.update(['d', 'e', 'f'])

# Removing 'b'
letters.discard('b')

# Output: {'a', 'c', 'd', 'e', 'f'}
print(letters)