# Write a program using the reduce() function and a lambda function to calculate the product of all elements in a list.
# Algorithm: 1_Import the reduce() function from the functools module. 2_Define a lambda function to multiply two numbers together. 3_Use the reduce() function to apply the lambda function to each pair of elements in the list. 4_Print the result.

from functools import reduce

#Define the lambda function to multiply two numbers together
multiply = lambda x, y: x * y

#List for which to calculate the product of elements
numbers = [1, 2, 3, 4, 5]

#Calculate the product of elements in the list
result = reduce(multiply, numbers)

#Alternative method: Using a Loop
result = 1
for num in numbers:
    result *= num

print(f"The product of elements in the list: {result}")