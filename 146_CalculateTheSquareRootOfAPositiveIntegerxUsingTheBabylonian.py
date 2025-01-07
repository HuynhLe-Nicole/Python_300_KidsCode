# Write a program to compute the square root of a positive integer x using the Babylonia algorithm. Then, compare the result of your program with the square root function from the math library. 
# Algorithm: 1_Initialize the guess value to x. 2_While the guess is not close enough to the square root of x, update the guess by taking the average of the guess and x/guess. 3_Print the result.

import math

def babylonia_sqrt(x):
    guess = x
    while abs(guess * guess - x) > 1e-10:
        guess = (guess + x / guess) / 2
    return guess

#Test
x = 16
print("Babylonian method:", babylonia_sqrt(x))
print("math.sqrt:", math.sqrt(x))