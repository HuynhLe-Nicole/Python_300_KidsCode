# Write a program that uses the reduce() function to compute the sum of elements in a list.
# Algorithm: 1_Take input as a list of numbers. 2_Define a function to add two numbers. 3_Use the reduce() function to apply the addition function to each element of the list. 4_Output the result as the total sum of the elements in the list.

from functools import reduce

def add(x, y):
    """
    Function to add two numbers.
    """
    return x + y

#Input list
numbers = [1, 2, 3, 4, 5]

#Use the reduce function to calculate the sum of elements in the list 
total = reduce(add, numbers)

#Additonal methods: Using the built-in sum() function
total = sum(numbers)

#Using a for loop
total = 0
for n in numbers:
    total += n

print("Sum of the elements in the list:", total)

