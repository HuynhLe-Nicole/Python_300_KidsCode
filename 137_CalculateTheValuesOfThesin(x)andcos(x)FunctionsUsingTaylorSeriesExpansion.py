# Write a program to calculate the values of the sin(x) and cos(x) functions using Taylor series expansion. The Taylor series is a way to represent functions as an infinite sum of polynomial terms.
# Algorithm: 1_Read the value of x from the user. 2_Read the number of terms in the Taylor series from the user. 3_Implement the Taylor series to calculate sin(x). 4_Implement the Taylor series to calculate cos(x). 5_Print the result of sin(x) and cos(x).

import math

def taylor_sin(x, terms):
    sin_x = 0
    for n in range(terms):
        sign = (-1) ** n
        sin_x += sign * (x **(2 * n + 1)) / math.factorial(2 * n + 1)
    return sin_x

def taylor_cos(x, temrs):
    cos_x = 0
    for n in range(terms):
        sign = (-1) ** n
        cos_x += sign * (x ** (2 * n)) / math.factorial(2 * n)
    return cos_x

#Get the value of x from the user (angle in radians)
x = float(input("Enter the value of x (in radians): "))

#Get the number of terms in the Taylor series
terms = int(input("Enter the number of terms in the taylor series: "))

#Calculate the sin(x) and cos(x) using the Taylor series
sin_x = taylor_sin(x, terms)
cos_x = taylor_cos(x, terms)

#Print the results
print(f"The value of sin({x}) using Taylor series with {terms} terms is: {sin_x}")
print(f"The value of cos({x}) using Taylor series with {terms} terms is: {cos_x}")