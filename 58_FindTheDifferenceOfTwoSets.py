# Write a program to find the difference of two sets. The difference of two sets A and B (often called the relative complement) is new set containing elements that appear only in set A but not in set B.
# Algorithm: 1_Use the two sets initialized from the previous code. 2_Find the difference of the two sets using the - operator or the difference() method.

#Initialize two initial sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'durian'}
print("Set 1:", set1)
print("Set 2:", set2)

#Find the difference of the two sets
set_difference = set1 - set2
# set_difference = set1.difference(set2)
print("Difference of the two sets:", set_difference)
