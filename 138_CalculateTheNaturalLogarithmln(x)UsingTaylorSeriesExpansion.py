# Write a program to calculate the natural logarithm ln(x) using Taylor series expansion.
# Algorithm: 1_Read the value of x from the user. 2_Check if  x > 0 and x # 1. 3_Implement the Taylor series to calculate ln(x): If x > 0 and x # 1, use the Taylor series to compute ln(x). 4_Print the result of ln(x)
# Taylor series for ln(x) converges slowly when x is near 1, but can be written using transformations. A simple method is to use the Taylor series for ln(1+y) when y = x-1 and |y| < 1: ln(1+y) = y - y^2/2 + y^3/3 - y^4/4+...

def taylor_ln(x, terms): 
    if x <= 0:
        raise ValueError("The value of x must be greater than 0")
    if x == 1:
        return 0
    
    #Use ln(x) = 2 * sum((y^n / n) for n in range(1, terms + 1))
    # where y = (x-1) / (x+1)
    y = (x-1) / (x+1)
    ln_x = 0
    for n in range(1, terms + 1):
        ln_x += (y **(2 * n -1)) / (2 * n -1)
    return 2 * ln_x

#Get the value of x from the user
x = float(input("Enter the value of x (x > 0 and x # 1): "))

#Get the number of terms in the Taylor series
terms = int(input("Enter the number of temrs in the taylor series: "))

#Calculate the value of ln(x) using the Taylor series
try:
    ln_x = taylor_ln(x, terms)
    print(f"The value of ln({x}) using Tayor series with {terms} terms is: {ln_x}")
except ValueError as e:
    print(e)