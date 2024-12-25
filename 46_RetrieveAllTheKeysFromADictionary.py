# Write a program to retrieve all the keys from a dictionary. Use the keys() method of dictionary to get a list of keys
# Algorithm: 1_Initialize a dictionary with initial key-value pairs. 2_Use the keys() method to obtain a list of all the keys from the dictionary. 3_Print the list of keys.

#Initialize a dictionary with initial key-value pairs
my_dict = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
}

#Print the initial dictionary
print("Initial Dictionary:", my_dict)

#Retrieve all keys in the dictionary
keys = my_dict.keys()

#Print the list of keys
print("Keys in the dictionary:", list(keys))