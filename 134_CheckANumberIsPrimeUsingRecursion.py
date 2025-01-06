# Write a program that checks if a number is prime using a recursive method.
# Algorithm: To check if a number is prime, recursively verify whether it is divisible by any number from 2 up to the square root of the number.

def is_prime_recursive(n, divisor=None):
    """
    Recursive function to check for a prime number.
    """
    if divisor is None: #If the divisor is not provide, initialize it to n -1 
        divisor = n - 1

    if n < 2: #Return False if n is less than 2, as prime numbers are greater than 1
        return False
    
    if divisor == 1: #If divisor reaches 1, return True, indicating that n is prime
        return True
    
    if n % divisor == 0: #If n is divisible by divisor, return false, indicating that n is not prime
        return False
    
    return is_prime_recursive(n, divisor - 1)

#Test the function with an input number
number = 29

if is_prime_recursive(number):
    print(f"{number} is a prime number.")
else: 
    print(f"{number} is not a prime number.")