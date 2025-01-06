# Write a program that calculates the sum of numbers from 1 to n, where n is a positive integer entered by the user.
# Algorithm: 1_Read the value of n from the user. 2_Check if n is a positive integer. 3_Calculate the sum of numbers from 1 to n. 4_Print the calculated sum.

def calculate_sum(n):
    #Calculate the sum of numbers from 1 to n
    return sum(range(1, n +1))

#Get the value of n from the user
n = int(input("Enter a positive integer n:"))

#Check if n is a positive integer
if n > 0:
    #Calculate the sum and print the result
    total_sum = calculate_sum(n)
    print(f"The sum of numbers from 1 to {n} is: {total_sum}")
else: 
    print("Please enter a positive integer.")
    