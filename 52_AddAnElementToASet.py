# Write a program that adds an element to a set using 2 different methods: 1_Using the add() method. 2_Using the update() method.
# Algorithm: 1_Initialize an initial set. 2_Use the add() method to add an element to the set. 3_Use the update() method to add an element to the set.

#Initialize an initial set
my_set = {'apple', 'banana', 'cherry'}
print("Initial set:", my_set)

#Method 1: Use the add() method to add an element to the set
my_set.add('orange')
print("Set after adding 'orange' using the add() method:", my_set)

#Method 2: Use the update() method to add an element to the set
my_set.update(['grape']) # The update() method requires an iterable, so the element needs to be in an iterable
print("Set after adding 'grape' using the update() method:", my_set)