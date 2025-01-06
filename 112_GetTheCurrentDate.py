# Write a program that retrieve the current day, month, year, hour, minute, and second, then outputs each value on a separate line.
# Algorithm: 1_Use the datetime library to get the current date and time. 2_Utilize the datetime.now() method to get the current time. 3_Access the date, month, year, hour, minute, and second components from the datetime object. 4_Print each component on its won line.

from datetime  import datetime

def get_current_date_time():
    """
    Function to retrieve the current day, month, year, hour, minute, and second and print each on a separate line.
    """
    #Get the current time
    current_time = datetime.now()

    #Access each component: year, month, day, hour, minute, second
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    #Print each component on a separate line 
    print("Year:", year)
    print("Month:", month)
    print("Day:", day)
    print("Hour:", hour)
    print("Minute:", minute)
    print("Second:", second)

#Call the function and print the results
get_current_date_time()