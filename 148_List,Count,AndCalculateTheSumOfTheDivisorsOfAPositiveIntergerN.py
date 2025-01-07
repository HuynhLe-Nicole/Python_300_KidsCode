# Write a program to list, count, and calculate the sum of divisors of a positive integer n.
# Algorithm: 1_Input a positive integer n from the keyboard. 2_Iterate through all numbers from 1 to n. 3_Check if the number is a divisor of n. 4_If it is, add the number to the divisor list, increase the divisor count by 2, and add it ot the sum of the divisors.

def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors, len(divisors), sum(divisors)

n = int(input("Enter a positive integer: "))
divisors, count, total = find_divisors(n)
print(f"Divisors of {n}: {divisors}")
print(f"Number of divisors: {count}")
print(f"Sum of divisors: {total}")
