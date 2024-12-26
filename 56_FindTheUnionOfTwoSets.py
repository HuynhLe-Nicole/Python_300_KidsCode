# Write a program to find the union of two sets
# Algorithm: 1_Initialize two initial set. 2_Find the union of the two sets using the | operator or the union() method

#Initialize two initial sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'durian'}
print("Set 1:", set1)
print("Set 2:", set2)

#Find the union of the two sets
set_union = set1 | set2
print("Union of the two sets:", set_union)