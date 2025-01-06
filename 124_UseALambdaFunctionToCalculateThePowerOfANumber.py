# Write a program that uses a lambda function to calculate the power of a number.
# Algorithm: 1_Take input as a base number and an exponent. 2_Define alambda function to compute the power of the base number. 3_Apply the lambda function to the base number and exponent. 4_Output the result as the power of the base number.

#Define a lambda function to calculate the power of a number
power = lambda x, y: x ** y

#Base number and exponent
number = 2
exponent = 3

#Calculate the power of the number
result = power(number, exponent)

print(f"{number} raised to the power of {exponent} is: {result}")