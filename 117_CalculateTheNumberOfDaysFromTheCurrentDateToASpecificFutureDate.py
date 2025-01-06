# Write a program to calculate the number of days from the current date to a specified future date.
# Algorithm: 1_Use the datetime library to get the current date. 2_Accept input as a date string in a fixed format representing the target date. 3_Convert the target date string into a datetime object. 
#4_Calculate the difference between the current date and the target date by subtracting the two datetime objects. 5_Output the result as the number of days of difference.

from datetime  import datetime

def calculate_days_to_target_date(target_date, format):
    """
    Function to calculate the number of days from the current date to a specific date.
    """
    #Get the current date
    current_date = datetime.now()

    #Convert the target date string into a datetime object
    target_date_obj = datetime.strftime(target_date, format)

    #Calculate the difference in days
    difference = target_date_obj - current_date

    return difference.days

#Input target date
target_date = "31-12-2024"
format - "%d-%m-%Y"

#Call the function and print the result
number_of_days = calculate_days_to_target_date(target_date, format)
print("The number of days from the current date to the target date is:", number_of_days)