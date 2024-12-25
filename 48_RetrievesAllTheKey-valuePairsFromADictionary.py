# Write a program that retrieves all the key-value pairs from a dictionary. Use the items() method of the dictionary to obtain a list of key-value pairs as tuples.
#Algorithm: 1_Initialize a dictionary with initial key-value pairs. 2_Use the items() method to get the list of key-value pairs from the dictionary. 3_Print the list of key-value pairs.

#Initialize a dictionary with initial key-value pairs
my_dict = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
}

#Print the initial dictionary
print("Initial Dictionary:", my_dict)

#Retrieve all key-value pairs in the dictionary
items = my_dict.items()

#Convert the key-value pairs to a list
items_list = list(items)

#Print the list of key-value pairs
print("List of key-value pairs in the dictionary:", items_list)