# Write a program to check if a file exists or not. Use the os module to check for the existence of a file.

import os
#Path to the file to check
file_path = 'example.txt'

#Check for the existence of the file
if os.path.isfile(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")