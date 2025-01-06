# Write a program that uses the map() function and a lambda function to double the elements in a list.
# Algorithm: 1_Define a lambda function to double a number. 2_Use the map() function to apply the lambda function to each element of the list. 3_Convert the result returned by map() to a list. 4_Output the resulting list.

#Define a lambda function to double a number
double = lambda x: x * 2

#List of numbers to be doubled
numbers = [1, 2, 3, 4, 5]

#Double the elements in the list
result = list(map(double, numbers))

#Alternative method: Using list comprehension is another way to achieve the same result: 
result = [x * 2 for x in numbers]

print(f"The list after doubling the elements: {result}")