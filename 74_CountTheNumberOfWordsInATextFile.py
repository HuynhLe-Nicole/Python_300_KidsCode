# Write a program to count the number of words in a text file. Use the open() function.
# Algorithm: 1_Open the text file using the open() function in read mode('r'). 2_Read each line of the file. 3_ Split each line into words. 4_Count the total number of words. 5_Print the word count.

#Path to the text file
file_path = 'example.txt'

try:
    #Open the text file in read mode
    with open(file_path, 'r') as file:
        #Initialize the word count variable
        word_count = 0
        #Read each line of the file
        for line in file:
            #Split the line into words and count the words
            words = line.split()
            word_count += len(words)
        #Print the word count
        print(f"Number of words in the file: {word_count}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
