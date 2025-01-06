# Write a program using the filter() function and a lambda function to filter out numbers greater than 10 from a list.
# Algorithm: 1_Define a lambda function to check if a number is greater than 10. 2_Use the filter() function to apply the lambda function to each element of the list. 3_Convert the result returned from filter() into a list. 4_Print the resulting list. 

#Define the lambda function to check if a number is greater than 10
greater_than_10 = lambda x: x > 10

#List to filter for number greater than 10
numbers = [5, 10, 15, 20, 25]

#Filter numbers greater than 10 in the list
result = list(filter(greater_than_10, numbers))

#Alternative methods: Using list comprehension
result = [x for x in numbers if x > 10]

print(f"The list after filtering numbers greater than 10: {result}")