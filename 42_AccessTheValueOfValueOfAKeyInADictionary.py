# Write a program to access the value of a key in a dictionary
# Algorithm: 1_Initialize a dictionary with a key-value pairs. 2_Input the key to access from the user. 3_Check if the key exist in the dictionary. 4_If the key exists, access and print the corresponding value. 5_If the key does not exist, notify that the key is not present in the dictionary.

#Initialize a dictionary with key-value pairs
my_dict = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
}

# Print the created dictionary
print("Created dictionary:", my_dict)

#Input the key to access from the user
key = input("Enter the key to access: ")

# Check if the key exists in the dictionary
if key in my_dict:
    #Access and print the corresponding value for the key
    value = my_dict[key]
    print(f"The value of the key '{key}' is: {value}")
else:
    #Notify that the key does not exist in the dictionary
    print(f"The key '{key}' does not exist  in the dictionary.")
    