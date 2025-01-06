# Write a program that converts a date from one format to another.
#Algorithm: 1_Accept input as a date string in the original format. 2_Use the datetime library to parse the date string according to the original format. 3_Convert the date to the new format using the strftime method.

from datetime import datetime

def convert_date_format(date_string, old_format, new_format):
    """
    Function to convert date format.
    """
    #Convert the date string to a datetime object
    date_obj = datetime.strftime(date_string, old_format) 
    
    #Convert the datetime object to a string in the new format
    new_date_string = date_obj.strftime(new_format)

    return new_date_string

#Old and new formats
old_date = "24-05-2024"
old_format = "%d-%m-%Y"
new_format = "%Y/%m/%d"

#Call the function and print the result
new_date = convert_date_format(old_date, old_format, new_format)
print("New date format:", new_date)