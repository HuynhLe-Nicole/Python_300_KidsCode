#Write a function to calculate the factorial of a number. The factorial of a positive integer n (n!) is the product of all positive integers from 1 to n.
#Algorithm: 1- Using a Loop. 2-Using a Recursion.

# Program to calculate the factorial of an integer using a loop
def factorial_iterative(n):
    if n < 0:
        return "Factorial is undefined for negative numbers."  #Error for negative input
    result = 1 #Initialize result
    for i in range(1, n+1): #Loop from 1 to n
        result *= i #Multiply result by each integer
    return result #Return the computed factorial

#Get a positive integer from the user
try:
    number = int(input("Enter a positive integer: "))  #Input and convert to integer
    if number < 0:
        print("Factorial is undefined for negative numbers.")  #Handle negative input
    else:
        print(f"The factorial of {number} is: {factorial_iterative(number)}") #Print the result
except ValueError:
    print("Please enter a valid integer.") #Error for non-integer input