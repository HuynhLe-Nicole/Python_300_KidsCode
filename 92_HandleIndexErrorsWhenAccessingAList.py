# Write a program to catch errors when trying to access and index that does not exist in a list.
# Algorithm: 1_Attempt to access an index in a list inside a try block. 2_Catch the IndexError in an except block.

try:
    my_list = [1, 2, 3]
    value = my_list[5] #Trying to access an index that doesn't exist
except IndexError:
    value = "Error: Index out of reange!"

print(value)