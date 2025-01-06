# Write a program that prints the calendar for a specific month of a specific year.
# Algorithm: 1_Use the calendar library. 2_Accept input for the year and month. 3_Use the month() method of the TextCalendar object to print the calendar for the specific month.

import calendar

def print_month_calendar(year, month):
    """
    Function to print the calendar of a specific month.
    """
    #Create a TextCalendar object starting with Sunday
    cal = calendar.TextCalendar(calendar.SUNDAY)

    #Get the calendar of the month as a string
    month_calendar = cal.formatmonth(year, month)

    #Print the calendar
    print(month_calendar)

#Input year and month
year = 2024
month = 5

#Call the function and print the result
print_month_calendar(year, month)
