# Write a program to find the solutions of a system of two linear equations with two variables, x and y.
#Algorithm: 1_Calculate the determinant D = a1b2 -a2b1. 2_If D = 0: the system has either infinitely many solutions or no solution. 
# 3_If D # 0: the system has a unique solution given by: x = (c1b2 - c2b1) / D, y = (a1c2 - a2c1) / D.

def solve_linear_system(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    if D == 0:
        return "The system has either infinitely many solutions or no solution."
    else:
        x = (c1 * b2 - c2 * b1) / D
        y = (a1 * c2 - a2 * c1) / D
        return f"The system has a unique solution: (x, y) = ({x}, {y})"
    
#Input coefficients a1, b1, c1, a2, b2, c2
a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))
a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

print(solve_linear_system(a1, b1, c1, a2, b2, c2))