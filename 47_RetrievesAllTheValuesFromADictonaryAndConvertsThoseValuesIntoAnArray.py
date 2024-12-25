# Write a program that retrieves all the values from a dictionary and converts those values into an array. Use the values() method of the dictionary to obtain the list of values.
# Algorithm: 1_Initialize a dictionary with initial key-value pairs. 2_Use the value() method to get the list of value from dictionary. 3_Convert the list of values into an array. 4_Print the array of values.

#Initialize a dictionary with initial key-value pairs
my_dict ={
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
}

#Print the initial dictionary
print("Initial Dictionary:", my_dict)

#Retrieve all values in the dictionary
values = my_dict.values()

#Convert the values to an array (list in Python)
values_array = list(values)

#Print the array of values
print("Array of values in the dictionary:", values_array)