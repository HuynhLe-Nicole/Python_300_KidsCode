# Write a program to find the intersection of two sets 
# Algorithm: 1_Use the two sets initialized from the previous code. 2_Find the intersection of the two sets using the & operator or the intersection() method

# Initialize two initial sets
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'durian'}
print("Set 1:", set1)
print("Set 2:", set2)

#Find the intersection of the two sets
set_intersection = set1 & set2
# set_intersection = set1.intersection(set2)
print("Intersection of the two sets:", set_intersection)