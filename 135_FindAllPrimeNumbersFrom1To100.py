# Write a program to find all prime numbers from 1 to 100.
# Algorithm: 1_Create a function to check if a number is prime. 2_Use a loop to check all numbers from 1 to 100. 3_If a number is prime, add it to the result lits. 4_Print the list of prime numbers found.

def is_prime(n):
    #Check if n is less than 2; if so, it's not a prime number
    if n < 2: 
        return False
    
    #Check for factors from 2 to the square root of n 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#List to store the prime numbers
prime_numbers = []

#Check all numbers from 1 to 100
for num in range(1, 101):
    if is_prime(num):
        prime_numbers.append(num)

#Print the list of prime numbers from 1 to 100
print(prime_numbers)