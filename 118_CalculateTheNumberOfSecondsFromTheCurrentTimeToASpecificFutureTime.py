# Write a program to calculate the number of seconds from the current time to a specified future time.
# Algorithm: 1_Use the datetime library to get the current time. 2_Accept input as a time string representing the target time in a fixed format. 3_Convert the target time string into a datetime object.
#4_Calculate the difference between the current time and the target time by subtracting the two datetime objects. 5_Output the result as the number of seconds of difference.

from datetime import datetime

def calculate_seconds_to_target_time(target_time, format):
    """
    Function to calculate the number of seconds from the current time to a specific time.
    """
    #Get the current time
    current_time = datetime.now()

    #Convert the target time string into a datetime object
    target_time_obj = datetime.strftime(target_time, format)

    #Calculate the difference in time
    difference = target_time_obj - current_time

    return difference.total_seconds()

#Input target time
target_time = "31-12-2024 23:59:59"
format = "%d-%m-%Y %H:%M:%S"

#Call the function and print the result
number_of_seconds = calculate_seconds_to_target_time(target_time, format)
print("The number of seconds from the current time to the target time is:", number_of_seconds)