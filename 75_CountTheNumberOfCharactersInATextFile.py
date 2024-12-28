# Write a program to count the number of characters in a text file. Use open() function.
# Algorithm: 1_ Open the text file using the open() function in read mode('r). 2_Read the entire content of the file. 3_Filter out whitespace and newline characters. 4_Count the total number of remaining characters. 5_Print the character count.

#Path to the text file
file_path = 'example.txt'

try:
    #Open the text file in read mode
    with open(file_path, 'r') as file:
        #Read the entire content of the file 
        content = file.read()
        #Filter out whitespace and newline characters
        filtered_content = ''.join(c for c in content if c not in ('', '\n', '\t'))
        #Count the number of characters in the filtered content
        char_count = len(filtered_content)
        #Print the character count
        print(f"Number of characters in the file (ignoring whitespace and newline): {char_count}")
except FileNotFoundError:
    print(f"File ot found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")