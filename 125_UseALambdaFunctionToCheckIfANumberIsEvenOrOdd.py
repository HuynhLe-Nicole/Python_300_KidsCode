# Write a program that uses a lambda function to determine whether a given number is even or odd.
# Algorithm: 1_Take input as a number. 2_Define a lambda function to check if the number is even or odd. 3_Apply the lambda function to the given number. 4_Output the result as "Even" if the number is even, and "Odd" if the number is odd.

#Define a lambda function to check if a number is even or odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

#Number to check
number = 3

#Check if the number is even or odd
result = is_even(number)

print(f"The number {number} is: {result}")
