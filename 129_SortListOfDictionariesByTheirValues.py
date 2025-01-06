# Write a program that uses a lambda function to sort a list of dictionaries by their values.
# Algorithm: 1_Define a lambda function to extract the value from a dictionary. 2_Use the sorted() function to sort the list of dictionaries by the specified value. 3_Print the sorted list.

# List of dictionaries to be sorted
dict_list = [{'name': 'John', 'age': 20}, {'name': 'Jane', 'age': 22}, {'name': 'Doe', 'age': 19}]

#Sort the list of dictionaries by the value of 'age'
sorted_list = sorted(dict_list, key=lambda x: x['age'])

#Alternative method: Using the sort() method of the list
dict_list.sort(key=lambda x: x['age'])

print(f"The list after sorting: {sorted_list}")
