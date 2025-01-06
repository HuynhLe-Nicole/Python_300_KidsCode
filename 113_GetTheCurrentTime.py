# Write a program that retrive the current time and displays it in two format: 24-hour and 12-hour (AM/PM)
# Algorithm: 1_Use the datetime library to get the current time. 2_Format the current time in the 24-hour format. 3_Format the current time  in the 12-hour format (AM/PM)

from datetime import datetime

def get_current_time():
    """
    Function to get the current time in both 24-hour and 12-hour (AM/PM) formats.
    """
    #Get the current time
    current_time = datetime.now()

    #Format time in 24-hour style
    time_24h = current_time.strftime("%H:%M:%S")

    #Format time in 12-hour style (AM/PM)
    time_12h = current_time.strftime("%I:%M:%S %p")

    return time_24h, time_12h

#Call the function and print the results
time_24h, time_12h = get_current_time()
print("Current time in 24-hour format:", time_24h)
print("Current time in 12-hour format (AM/PM):", time_12h)
