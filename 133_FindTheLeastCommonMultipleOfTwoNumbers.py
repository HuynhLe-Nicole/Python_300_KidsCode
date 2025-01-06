# Write a program to find the least common multiple (LCM) of two given numbers. LCM a and b, is the smallest number that is divisible by both a and b.
# Algorithm: 1_Use the formula: LCM(a,b) = (a * b)/GCD(a, b), where GCD is the greatest common divisor. 2_Use the gcd function from the math library to calculate the GCD.

import math #Import the math library to use the gcd function

def lcm(a, b):
    """
    Function to find the least common multiple (LCM) of two numbers.
    """
    return abs(a * b) // math.gcd(a, b)

#Input two numbers
a = 15
b = 20

#Call the function and print the result
bscnn = lcm(a, b) 
print (f"The least common multiple of {a} and {b} is: {bscnn}")