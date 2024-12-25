# Write a program to add a key-value pair to dictionary.
#Algorithm: 1_Initialize a dictionary with intial key-value pairs(which can also be empty). 2_Input the key and value from user. 3_Add the key-value pair to the dictionary. 4_Print the dictionary after adding the key-value pair

#Initial a dictionary with initial key-value pairs
my_dict = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
}

# Print the initial dictionary
print("Initial dictionary:", my_dict)

#Input the key to add from the user
new_key = input("Enter the key to add: ")

#Input the value to add from user
new_value = input("Enter the value to add: ")

#Add the key-value pair to the dictionary
my_dict[new_key] = new_key

#Print the dictionary after adding the key-value pair
print("Dictionary after adding the key-value pair:", my_dict)