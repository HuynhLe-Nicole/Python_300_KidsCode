# Write a program to input a positive integer n and then factor n into its prime factors.
# Algorithm: 1_Input the positive integer n from the user. 2_Iterate through all integers starting from 2. 3_Check if the integer is a prime factor of n. 4_If it is, add it to the list of prime factors and divide n by that integer
# 5_Repeat steps 3 and 4  until n is not longer divisible by that integer. 6_Print the list of prime factors.

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)
    return factors

n = int(input("Enter a positive integer: "))
factors = prime_factors(n)
print(f"Prime factors of {n}: {factors}")