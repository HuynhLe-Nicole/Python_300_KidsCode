# Write a program to print  all Armstrong numbers from 1 to 1000. Armstrong number (also know as a Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. Ex: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153
# Algorithm: Initialize an empty list to store Armstrong numbers, 2_Use a loop to check each number from 1 to 1000. 
# 3_For each number: Calculate the number of digits. Compute the sum of each digit raised to the power of the number of digits. If this sum is equal to the number itself, add it to the list. 4_Print the list of Armstrong numbers.

def is_armstrong_number(num):
    #Convert the number to a string to easily access each digit
    num_str = str(num)

    #Calculate the number of digits
    num_digits = len(num_str)

    #Calculate the sum of the digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    #Check if the sum equals the number itself
    return sum_of_powers == num

#List to store Armstrong numbers
armstrong_numbers = []

#Check numbers from 1 to 1000
for num in range(1, 1001):
    if is_armstrong_number(num):
        armstrong_numbers.append(num)

#Print the list of Armstrong numbers from 1 to 1000
print(f"The Armstrong nnumbers from 1 to 1000 are: {armstrong_numbers}")