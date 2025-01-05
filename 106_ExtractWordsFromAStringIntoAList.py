# Write a program that extracts words from a string into list.
# Algorithm: 1_Read the content from the text file. 2_Split the string into a list of words using the split method. 3_Print the list of words.

#Method1: Using the split method

def read_file(file_name):
    """
    Function to read content from a text file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content 

def extract_words(file_name):
    """
    Function to extract words from a string into a list.
    """

    content = read_file(file_name)

    #Split the string into a list of words
    word_list = content.split()

    return word_list

#File path to the text file
file_name = 'example.txt'

#Call the function and print the result
word_list = extract_words(file_name)
print(word_list)


#Method2: Using the re library for more complex processing

import re

def read_file(file_name):
    """
    Function to read content from a text file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_words(file_name):
    """
    Function to extract words from a string into a list.
    """
    content = read_file(file_name)

    #Use regular expression to extract words
    word_list = re.findall(r'\b\w+\b', content)

    return word_list

#File path to the text file
file_name = 'example.txt'

#Call the function and print the result
word_list = extract_words(file_name)
print(word_list)
