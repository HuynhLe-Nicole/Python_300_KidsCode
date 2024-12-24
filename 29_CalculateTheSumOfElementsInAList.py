# Write a program to calculate the sum of the element in a list.
# Algorithm: 1_Initialize the list with random elements. 2_Use the sum() function to calculate the sum of the elements in the list. 3_Print the sum of the elements.

import random
#Initialize the list with random elements
#Assume the list has 10 element with values from 1 to 100
my_list = [random.randint(1, 100) for _ in range(10)]

#Print the initial list
print("Initial list:", my_list)

#Calculate the sum of the elements in the list
total_sum = sum(my_list)

#Print the sum of the elements
print("The sum of the elements in the list is:", total_sum)