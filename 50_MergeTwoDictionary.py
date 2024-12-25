# Write a program that merges two dictionaries into one. Use: 1_Use the update() method. 2_Use the ** operator to unpack the dictionaries and merge them together.
# Algorithm: 1_Initialize two dictionaries with some initial key-value pairs. 2_Use the update() method to merge the two dictionaries. 3_Use the ** operator to merge the two dictionaries.

#Initialize two dictionaries with some initial key-value pairs 
dict1 = {
    'name' : 'Alice',
    'age' : 25
}
dict2 = {
    'city' : 'New York',
    'country' : 'USA'
}

#Print the initial two dictionaries
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

#Method 1: Use the update() method to merge two dictionaries
dict3 = dict1.copy()  # Create a copy of dict1 to avoid changing the original
dict1
dict3.update(dict2)
print("Result of merging dictionaries using update():", dict3)

#Method 2: Use the ** operator to merge two dictionaries
dict4 = {**dict1, **dict2}
print("Result of merging dictionaries using the ** operator:", dict4)