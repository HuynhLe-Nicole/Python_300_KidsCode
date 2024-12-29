# Write a program that copies the content from one file to another. Use the open() function
# Algorithm: 1_Open the source file using the open() function in read mode('r). 2_Open the destination file using the open() function in  write mode('w'). 3_Read the entire content from source file. 
#4_Write the entire content to the destination file. 5_Close both files after the operation.

#Path to the source and destination files
source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

try:
    #Open the source file in the read mode
    with open(source_file_path, 'r') as source_file:
        #Read the entire content of the source file
        content = source_file.read()

    #Open the destination file in write mode
    with open(destination_file_path, 'w') as destination_file:
        #Write the entire content into the destination file
        destination_file.write(content)

    print(f"Content has been copied from '{source_file_path}' to {destination_file_path}'.")
except FileNotFoundError:
    print(f"File not found: {source_file_path} or {destination_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")