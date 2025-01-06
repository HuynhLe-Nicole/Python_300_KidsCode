# Write a program to calculate the time difference between two times.
# Algorithm: 1_Receive input as two time strings in a fixed format. 2_Use the datetime library to convert the time strings into datetime objects. 3_Calculate the difference between the two times by subtracting the two datetime objects. 4_Output the result as the time difference between the two times.

from datetime import datetime

def calculate_time_difference(time1, time2, format):
    """
    Function to calculate the time difference between two times.
    """
    #Convert time strings into datetime objects
    time1_obj = datetime.strftime(time1, format)
    time2_obj = datetime.strftime(time2, format)

    #Calculate time difference
    difference = time2_obj - time1_obj

    return difference

#Input times
time1 = "14:30:00"
time2 = "18:45:00"
format = "%H%M:%S"

#Call the function and print the result
difference = calculate_time_difference(time1, time2, format)
print("The time difference between the two times is:", difference)