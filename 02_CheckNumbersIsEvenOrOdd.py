#Write a program that checks whether a number entered by the user is even or odd
#Algorithm:
#1. Take an integer input from user.
#2. Check if the number is divisible by 2. If it is, print "The number is even".
#3. If the number is not divisible by 2, print "The number is odd".

#Define a function check_even_odd(n) that takes an integer n as input
def check_even_odd(n):
    #Check if n is divisible by 2
    if n % 2 == 0: # % operation is used to find the remainder of n when divided by 2
        return "The number is even"
    else:
        return "The number is odd"
    
#Take an integer input from the user
try:
    number = int(input("Enter a numer: "))
    #Call the check_even_odd function with the input number and store the result
    result = check_even_odd(number)
    #Print the result
    print(result)
except ValueError:
    #Handle error if the input is not an integer
    print("Please enter a valid integer.")