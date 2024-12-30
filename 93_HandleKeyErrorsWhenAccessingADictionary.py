# Write a program to catch errors when trying to access a key that does not exist in a dictionary.
# Algorithm: 1_Attempt to access a key in a dictionary inside a try block. 2_Catch the KeyError in an except block.

try:
    my_dict = {'name': 'John', 'age': 30}
    value = my_dict['address'] #Trying to access a key that doesn't exist
except KeyError:
    value = "Error: Key not found in dictionary!"

print(value)