# Write a program to fetch the current date and time.
#Algorithm: 1_Use the datetime library to get the current date and time. 2_Use the datetime.now() method to retrieve the current time. 3_Format and print the current date and time.

from datetime import datetime  #Imports the datetime class from the datetime library 

def get_current_date_time():
    """
    Function to fetch the current date and time.
    """
    #Fetch the current time
    current_time = datetime.now() #datetime.now(): method used to retrieve the current local date and time

    #Format the current date and time
    formatted_date_time = current_time.strftime("%Y-%m-%d %H:%M:%S") #strftime("%Y-%m-%d %H:%M:%S"): method formats the current date and time
    return formatted_date_time

#Call the function and print the result
print("Current date and time is:", get_current_date_time) #get_current_date_time: function returns the formatted current date and time