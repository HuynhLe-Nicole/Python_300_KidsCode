# Write a program to print the first n perfect numbers. Perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself. Ex: 6 is a perfect number because its divisors 1, 2, and 3 add up to 6.
# Algorithm: 1_Read the integer value of n from the user. 2_Initialize an empty list to store the perfect numbers. 3_Initilaize a counter to check consecutive positive integers. 
# 4_Use a loop to find perfect numbers: For each positive integer, calculate the sum of its positive divisors. If the sum equals the integer itself, add it to the list of perfect numbers. Continue the loop until the list contains n perfect numbers. 
# 5_Print the list of the first n perfect numbers.

def is_perfect_number(num):
    #Calculate the sum of positive divisors of sum (excluding itself)
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num

def find_perfect_numbers(n):
    perfect_numbers = []
    number = 1
    while len(perfect_numbers) < n:
        if is_perfect_number(number):
            perfect_numbers.append(number)
        number += 1
    return perfect_numbers

#Get the value of n from the user
n = int(input("Enter the number of perfect numbers to find: "))

#Find and print the first n perfect numbers
perfect_numbers = find_perfect_numbers(n)
print(f"The first {n} perfect numbers are: {perfect_numbers}")