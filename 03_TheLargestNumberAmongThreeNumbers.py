#Write a program that finds the largest number among three numbers entered by the user\
#Algorithm:
#1. Take three integer inputs from the users.
#2. Compare the three numbers to find the largest one.
#3. Print the largest number

#Define a fucntion find_max_of_three(a, b, c) that takes three integers a, b, and c as input
def find_max_of_three(a, b, c):
    #Compare the three numbers using if - elif - else statments
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else: 
        return c
    
#Take three integer inputs from the users
try: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    #Call the find_max_of_three function with the input numbers and store the result
    max_number = find_max_of_three(num1, num2, num3)
    print(f"The largest number is: {max_number}")
except ValueError:
    #Handle error if the input is not an integer
    print("Please enter valid integers.")
    