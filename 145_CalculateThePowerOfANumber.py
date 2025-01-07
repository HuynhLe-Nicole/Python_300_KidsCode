# Write a program to compute the power of a number.
# Algorithm: 1_Use the ** operator or the pow function to calculate the power of the number. 2_Print the result.

def power(base, exponent):
    return base ** exponent

#Alternative method: use pow function
def power(base, exponent):
    return pow(base, exponent)

#Test 
print(power(2, 3))