# Write a program that handles errors when attempting to read a file that does not exist.
# Algorithm: 1_Attempt to read a file inside a try block. 2_Catch the FileNotFoundError in an except block.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "Error: File not found!"

    return content

#Attempting to read a non-existent file
print(read_file('non_existent_file.txt'))