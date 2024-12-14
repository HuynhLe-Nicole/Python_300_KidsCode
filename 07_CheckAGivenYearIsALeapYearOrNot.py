#Write a program to check whether a given year is a leap year or not.
#A year is considered a leap year if: it is divisible by 4 and not divisible by 100, or divisible by 400
#Algorithm: 1.Input the year from user - 2.Check if the year is a leap year based on the criteria given - 3. Print the result.

#Program to check if a a year is a leap year
def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

#Input year from the user
try:
    year = int(input("Enter a year: "))  # Get input from the user and covert to an integer
    if is_leap_year(year): #Call the leap year checking function
        print(f"The year {year} is not a leap year.")  # Print if it is a leap year
    else:
        print(f"The year {year} is not a leap year.") # Print if it is not a leap year
except ValueError:
    print("Please enter a valid integer.") # Handle invalid input