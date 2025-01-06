# Write a program that calculates the time difference between two given dates.
# Algorithm: 1_Accept input as two date strings in a fixed format. 2_Use the datetime library to convert the date strings into datetime objects. 3_Calculate the difference between the two dates by subtracting the two datetime objects. 4_Output the result as the time difference between the two dates.

from datetime import datetime

def calculate_time_difference(date1, date2, date_format):
    """
    Function to calculate the time difference between two dates.
    """
    #Convert the date strings to datetime objects
    date1_obj = datetime.strftime(date1, date_format)
    date2_obj = datetime.strftime(date2, date_format)
    
    #Calculate the time difference
    time_difference = date2_obj - date1_obj

    return time_difference

#Input dates
date1 = "01-01-2020"
date2 = "24-05-2024"
date_format = "%d-%m-%Y"

#Call the function and print the result
time_difference = calculate_time_difference(date1, date2, date_format)
print("The time difference between the two dates is:", time_difference)