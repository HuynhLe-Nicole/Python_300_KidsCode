# Write a program to delete a key-value pair from a dictionary. Use the pop() method or the del keyword to remove a key-value pair from the dictionary.
# Algorithm: 1_Initialize a dictionary with initial key-value pairs. 2_Input the key to be deleted from the user. 3_Check if the key exists in the dictionary. 4_If the key exists, delete the corresponding key-value pair. 5_Print the dictionary after deleting the key-value pair.

# Initialize a dictionary with initial key-value pairs
my_dict = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
}

# Print the initial dictionary
print("Initial dictionary:", my_dict)

# Input the key to delete from the user
key_to_delete = input("Enter the key to delete: ")

#Check if the key exists in the dictionary 
if key_to_delete in my_dict:
    #Delete the key-value pair using the pop() method 
    my_dict.pop(key_to_delete)
    print(f"Delete the key-value pair with key '{key_to_delete}'.")
else:
    #Notify that the key does not exist in the dictionary
    print(f"The key '{key_to_delete}' does not exist in the dictionary.")

#Print the dictionary after deleting the key-value pair
print("Dictionary after deleting the key-value pair:", my_dict)