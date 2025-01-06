# Write a program that prints the calendar for a specific year.
# Algorithm: 1_Use the calendar library. 2_Accept input for the year. 3_Use the formatyear() method of the TextCalendar object to print the calendar for the specified year. 

import calendar

def print_year_calendar(year):
    """
    Function to print the calendar of a specific year.
    """
    #Create a TextCalendar object starting with Sunday
    cal = calendar.TextCalendar(calendar.SUNDAY)

    #Get the calendar for the year as a string
    year_calendar = cal.formatyear(year)

    #Print the calendar
    print(year_calendar)


#Input year
year = 2024

#Call the function and print the result
print_year_calendar(year)