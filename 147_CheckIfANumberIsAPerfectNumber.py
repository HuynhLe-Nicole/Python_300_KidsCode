# Write a program to determine if a number is a perfect number. A perfect number is a number that is equal to the sum of its proper divisors(excluding itself). Use a recursive algorithm.
# Algorithm: 1_Calculate the sum of the divisors of n using a recursive function. 2_Check if the sum is equal to n. 3_Print the result.

def  sum_of_divisors(n, i = 1, sum = 0):
    if i == n:
        return sum
    else:
        if n % i == 0:
            sum += i
        return sum_of_divisors(n, i + 1, sum)
    
def is_perfect(n):
    return sum_of_divisors(n) == n

#Test
print(is_perfect(6)) #True
print(is_perfect(28)) #True
print(is_perfect(12)) #False