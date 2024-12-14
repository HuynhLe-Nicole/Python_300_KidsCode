#Write a program to print all prime numbers from 1 to 100
#Definition of prime number: It is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself
#Algorithm: 1- Iterate through all numbers from 1 to 100. 2-Check if each number is a prime number. 3-If the number is prime, print it.

#Program to print all prime numbers from 1 to 100
def is_prime(n):
    if n <= 1: #Check if the number is less than or equal to 1
        return False  #Not a prime number
    for i in range(2, int(n**0.5) + 1):  # Check for factors from 2 up to the square root of n
        if n % i == 0: #If n is divisible by i 
            return False #It's not a prime number
    return True # n is a prime number

def print_prime_up_to_100():
    for number in range(1, 101): #Loop through numbers from 1 to 100
        if is_prime(number): # Check if number is prime using the is_prime function
            print(number, end='')  # Print the prime number on the same line
    print() #Print a newline after showing all prime numbers

# Call the function to print prime numbers from 1 to 100
print_prime_up_to_100()

#Logic:
    #If n is less than  or equal to 1, it return False because these numbers are not considered prime.
    #The loop from 2 to the square root of n. The square root is used because if n is divisible by any number larger than its square root, it must also be divisible by a number smaller than its square root.
    #If n is divisible by any i in that range(meaning n % i == 0), it return False.
    #If no divisors are found, it returns True, indicating n is prime.