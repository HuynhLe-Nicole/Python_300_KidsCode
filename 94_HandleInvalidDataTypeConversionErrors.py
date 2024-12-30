# Write a program that catches errors when attempting to perform invalid data type conversions. 
# Algorithm: 1_Attempt to perform data type conversion inside a try block. 2_Catch the ValueError in an except block.

try:
    value = int('abc') #Trying to convert a non-numeric string to an integer
except ValueError:
    value = "Error: Invalid type conversion!"

print(value)