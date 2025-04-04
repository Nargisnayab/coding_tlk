# Program Name:    Subsets and Supersets
# Purpose:       Work with subsets and supersets
# creator:          NN
# Date:       3-Apr-2025
#_____________________________________________________________________
# Create two sets
set_a = {1, 2, 3}
set_b = { 2, 3, 4,}

# True
print("Is set_a a subset of set_b?", set_a.issubset(set_b))
# True
print("Is set_b a superset of set_a?", set_b.issuperset(set_a))