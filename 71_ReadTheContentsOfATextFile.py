#Write a program that reads the contents of a text file. Use open() function to open the file and the read() method to read its content.
#Algorithm: 1_Open the text file using the open() function in read mode ('r'). 2_Use the read() method to read the entire content of the file. 3_Print the read content. 4_Close the file to free up resource.

#Path to the text file
file_path = 'example.txt'

try:
    #Open the text file in read mode
    with open(file_path, 'r') as file:
        #Read the entire content of the life
        conten = file.read()
        #Print the content of the file
        print("Content of the file:")
        print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")