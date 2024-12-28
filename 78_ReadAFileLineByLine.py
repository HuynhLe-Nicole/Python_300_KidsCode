# Write a program to read a text file line by line. Use open() function to open the file and the readline() method or a for loop to iterate over the file object to read each line.
# Algorithm: 1_Open the text file using the open() function in read mode('r'). 2_Use a for loop to iterate over each line in the file object. 3_Print each line to the screen.

#Path to the text file
file_path = 'example.txt'

try:
    #Open the text file in read mode
    with open(file_path, 'r') as file:
        #Iterate over each line in the file
        for line in file:
            #Print each line to the screen
            print(line, end='')
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")