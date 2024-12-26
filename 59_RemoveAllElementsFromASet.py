# Write a program that removes all elements from a set
# Algorithm: 1_Initialize a set. 2_Remove all elements in the set using the clear() method

#Initialize the set
set1 = {1, 2, 3, 4, 5}
print("Initial set:", set1)

#Remove all elements from the set
set1.clear()
# for item in set(list(set1)): (using remove() method)
    # set1.remove(item)
print("Set after removing all elements:", set1)