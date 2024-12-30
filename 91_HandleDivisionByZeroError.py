# Write a program to handle division by zero errors. When you attempt to divide a number by zero, the program will raise a ZeroDivisionError.
# Algorithm: 1_Perform the division operation inside a try block. 2_Catch the ZeroDivisionError in an except block.

try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Division by zero is not allowed!"

print(result)