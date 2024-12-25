# Write a program to check if an element exists in a set. Use the in operator to verify if the element is present in the set.
# Algorithm: 1_Initialize an initial set. 2_Use the in operator to check for the exsitence of the element in the set. 3_Print the rsult of the check.

#Intialize an initial set
my_set = {'apple', 'banana', 'cherry'}
print("Initial set:", my_set)

#Check for the existence of an element in the set
element = 'banana'
if element in my_set:
    print(f"Element '{element}' exists in the set.")
else:
    print(f"Element '{element}' does not exist in the set.")

element = 'orange'
if element in my_set:
    print(f"Element '{element}' exists in the set.")
else: 
    print(f"Element '{element}' does not exist in the set.")