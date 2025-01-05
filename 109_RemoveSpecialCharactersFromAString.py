# Write a program that removes special characters from a string, keeping only alphanumeric characters (letters and numbers)
# Algorithm: 1_Receive input as a string containing special characters. 2_Use regular expressions(re) to remove non-alphanumeric characters. 3_Print the resulting string.

import re

def remove_special_characters(string):
    """
    Function to remove special charcters from a string, keeping only letters and numbers.
    """
    result_string = re.sub(r'[^A-Za-z0-9]', '', string)
    return result_string

#Initial string containing special characters
original_string = "Hello, World! This is a string #123 with special character @2024."

#Call the function and print the result
result_string = remove_special_characters(initial_string)
print(result_string)