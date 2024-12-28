# Write a program to delete a text file. Use the os module.
# Algorithm: 1_Use the os module to check for the existence of the file. 2_If the file exists, use the os.romove() function to delete the file. 3_Print a confirmation message indicating that the file has been deleted or that is does not exist.

import os
#Path to the file to delete
file_path = 'example.txt'

try:
    #Check for the existence of the file
    if os.path.isfile(file_path):
        #Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")