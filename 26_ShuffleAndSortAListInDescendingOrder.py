# Write s program tha randomly shuffles a list and then sorts it in descending order. Use the sort(reverse=True) method to sort a list in descending order and the shuffle() function from  the random module to shuffle the list random
# Algorithm: 1_Initialize the List: Start with a list of numbers. 2_Shuffle the List: Use random.shuffle() to shuffle the list randomly. 
# 3_Sort the List: Use the sort(reverse=True) method to sort the list in descending order. 4_Print the Results: Print the list after shuffling and after sorting.

import random

# Initialize the list
my_list = [34, 1, 23, 4, 3, 12, 45, 33, 6, 22]

# Print the original list
print("Original list:", my_list)

#Shuffle the list randomly
random.shuffle(my_list)
print("List after shuffling:", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)

# Print the sorted list
print("List after sorting in descending order:", my_list)