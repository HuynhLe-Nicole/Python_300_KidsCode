# Write a program to check whether a key exists in a dictionary. Use the in operation to check the existence of a key in the dictionary.
# Algorithm: 1_Initalize a dictionary with intial key-value pairs. 2_Input the key to check from the user. 3_Use the in operator to check if the key exists in the dictionary. 4_Print a message indicating the result of the check.

#Initialize a dictionary with initial key-value pairs
my_dict = {
    'name' : 'Alice',
    'age' : 25,
    'city' : 'New York'
} 

#Print the initial dictionary
print("Initial dictionary:", my_dict)

#Input the key to check from the user
key_to_check = input("Enter the key to check: ")

#Check if the key exists in the dictonary
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")