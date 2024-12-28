#Write a program that writes content to a text file. Use the open() function to open a file in write mode and the write() method to write content to the file
#Algorithm: 1_Open the text file using the open() function in write mode ('w'). 2_Use the write() method to write content to the file. 3_Close the file to save changes and free up resources.

#Path to the text file
file_path = 'example_output.txt'

#Content to write to the file
content_to_write = "Hello, world!\nWelcome to the world of Python programming."

try:
    #Open the text file in write mode
    with open(file_path, 'w') as file:
        #Write content to the file
        file.write(content_to_write)
        #Print success messaga
        print(f"Content has been written to the file: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")