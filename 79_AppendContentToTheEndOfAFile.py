# Write a program that appends content to the end of a file. Use the open() function with the append mode('a') to open the file and the write() method to write new content to it.
# Algorithm: 1_Open the text file using open() function in append mode('a'). 2_Use the write() method to add new content at the end of the file. 3_Close the file after writing.

#Path to the text file
file_path = 'example.txt'
#Content to append
content_to_add = "\nThis is the new content added to the file."

try:
    #Open the text file in append mode
    with open(file_path, 'a') as file:
        #Write the new content to the end of the file
        file.write(content_to_add)
    print(f"Content has been appended to the file '{file_path}'.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
