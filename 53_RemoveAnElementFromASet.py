# Write a program that removes an element from a set using 2 different methods: 1_Using the remove() method. 2_Using the discard() method.
# Algorithm: 1_Initialize an initial set. 2_Use the remove() method to delete an element from the set. 3_Use the discard() method to delete an element from the set.

#Initialize an initial set
my_set = {'apple', 'banana', 'cherry'}
print("Initial set:", my_set)

#Method 1: Use the remove() method to remove an element from the set
my_set.remove('banana')
print("Set after removing 'banana' using the remove() method:", my_set)

#Method 2: Use the discard() method to remove an element from the set
my_set.discard('apple')
print("Set after removing 'apple' using the discard() method:", my_set)