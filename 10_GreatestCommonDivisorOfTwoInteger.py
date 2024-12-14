#Write a program to find the greates common divisor(GCD) of two integers
#Definition of GCD: The GCD of two integers a and b is the largest number that divides both a and b  without leaving a remainder.
#Algorithm: Use Euclid's algorithm =>  1- If b = 0, then GCD(a, b) = a. 2- Compute GCD(b, a % b).

#Program to find the greatest common divisor (GCD) of two integers
def gcd(a, b): 
    while b!= 0: #Loop until b is not 0
        a, b = b, a % b #Update a to b, and b to the remainder when a is divided by b 
    return a

#Get two integers from the user
try:
    num1 = int(input("Enter the first number: "))  #Input first number and covert to integer
    num2 = int(input("Enter the second number: ")) #Input second number and covert to integer

    uscln = gcd(num1, num2) # Call gcd function with user inputs
    print(f"The greatest common divisor of {num1} and {num2} is: {uscln}")  #Print the GCD
except ValueError:  #Handle invalid input
    print("Please enter valid integers.")  #Print error message if input is not an integer 