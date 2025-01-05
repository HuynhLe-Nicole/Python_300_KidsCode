# Write a prorgram that finds all the longest words in a string.
# Algorithm: 1_Read the content from the text file. 2_Split the string into a list of words. 3_Determine the lenght of the longest word. 
# 4_Find all words that have the same length as the longest words. 5_Print the result.

#Method1 : Using a Loop to find the longest words

def read_file(file_name):
    """
    Function to read content from a text file.
    """

    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def find_longest_words(file_name):
    """
    Function to find all longest words in a text file.
    """

    content = read_file(file_name)

    #Split the string into a list of words
    words_list = content.split()

    #Find the length of the longest words
    max_length = 0
    for word in words_list:
        if len(word) > max_length: 
            max_length = len(word)


    # Find all words with the same length as the longest word
    longest_words  = [word for word in words_list if len(word) == max_length]

    return longest_words

#Path to the text file
file_name = 'example.txt'

#Call the function and print the result
longest_words = find_longest_words(file_name)
print(f"The longest words in the file are: {longest_words}")

#Method2: Using max() with key

def read_file(file_name):
    """
    Function to read content from a text file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def find_longest_words(file_name):
    """
    Function to find all longest words in a text file.
    """
    content = read_file(file_name)

    #Split the string into a list of words
    words_list = content.split()

    #Find the length of the longest word using max with key as word length
    max_length = len(max(words_list, key=len))

    #Find all words with the same length as the longest word
    longest_words = [word for word in words_list if len(word) == max_length]

    return longest_words
