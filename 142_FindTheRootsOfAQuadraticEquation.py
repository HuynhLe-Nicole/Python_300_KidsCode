# Write a program that finds the roots of a quadratic equation in the form ax^2 + bx + c = 0
# Algorithm: 1_Calculate the discriminant delta = b^2 - 4ac. 2_If delta < 0, the equation has no real roots. 3_If delta = 0, the equation has one root x = -b/2a. 4_If delta > 0, the equation has 2 roots: x1,2 =(-b-+(square root delta))/2a. 5_Print the results.

import math

def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c  #Calculate the discriminant
    if delta < 0:
        return "The equation has no real solutions."
    elif delta == 0:
        x = -b / (2*a)
        return f"The equation has one repeated solution: x = {x}"
    else: 
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return f"The equation has two distinct solutions: x1 = {x1}, x2 = {x2}"
    
#Input a, b, and c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(solve_quadratic(a, b, c))
