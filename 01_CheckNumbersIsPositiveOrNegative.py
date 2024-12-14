#Write a program that checks whether a number entered by the user is positive or negative
#Algorithm:
#1. Take the integer input from the user.
#2. Check if the number is greater than 0. If it is, print "The number is positive".
#3. If the number is less than 0, print "The number is negative".
#4. If the number is equal to 0, print "The number is zero".

#Define a function check_number(n) that takes an integer n as input
def check_number(n):
    #Check if n is greater than 0
    if n > 0:
        return "The number is positive"
    
    #Check if n is less than 0
    elif n < 0:
        return "The number is negative"
    
    #If n is equal to 0, return a special message
    else:
        return "The number is zero"
    
#Take an integer input from the user
try:
    number = int(input("Enter a number: "))
    #Call the check number function with the input number and store the result
    result = check_number(number)
    #Print the result
    print(result)
except ValueError:
    #Handle error if the input is not an integer
    print("Please enter a valid integer.")