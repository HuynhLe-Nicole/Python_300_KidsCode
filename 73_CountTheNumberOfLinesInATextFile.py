# Write a program to count the number of lines in a text file. Use the open() function to open the file and read each line to count the number of lines.
# Algorithm: 1_Open the text file using the open() function in read mode('r'). 2_Read each line of the file and count the total number of lines. 3_Print the line count.

#Path to the text file
file_path = 'example.txt'

try:
    # Open the text file in read mode
    with open(file_path, 'r') as file:
        #Count the number of lines in the file
        line_count = sum(1 for line in file)
        #Print the line count
        print(f"NUmber of lines in the file: {line_count}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


#Another way to count the lines in a file is to read the entire content of the file into a list of lines and count the length of that list
try:
    #Open the text file in read mode
    with open(file_path, 'r')as file:
        #Read the entire content of the file into a list of lines
        lines = file.readline()
        #Count the number of lines
        line_count = len(lines)
        #Print the line count
        print(f"Number of lines in the file: {line_count}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")