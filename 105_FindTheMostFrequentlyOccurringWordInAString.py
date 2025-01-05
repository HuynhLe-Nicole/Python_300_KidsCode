# Write a program that finds the word that appears most frequently in a string. 
# Algorithm: 1_Read the content from the text file. 2_Split the string into a list of words. 3_Use a dictionary to count the occurrences of each word. 
# 4_Find the word with the highest occurence. 5_Print the result.

#Method1 : Using a dictionary to count word occurrence

def read_file(file_name):
    """
    Function to read content from a text file
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def find_most_frequent_word(file_name):
    """
    Function to find the most frequently occurring word int a text file.
    """
    content = read_file(file_name)

    #Split the string into a list of words
    word_list = content.split()

    #Use a dictionary to count the occurrences of each word
    word_count = {}
    for word in word_list:
        word = word.lower().strip('. , ! ? : ; () []') #Cover to lowercase and remove puctuation
        if word in word_count:
            word_count[word] += 1
        else: 
            word_count[word] = 1
        
    # Find the word that appears most frequently
    most_frequent_word = max(word_count, key=word_count.get)
    
    return most_frequent_word, word_count[most_frequent_word]

#Path to the text file
file_name = 'example.txt'

#Call the function and print the result
most_frequent_word, occurrent_count = find_most_frequent_word(file_name)
print(f"The most frequent word is: '{most_frequent_word}' with {occurrent_count} occurrences")

#Method2: Using counter from the collections library

from collections import Counter

def find_most_frequent_word(file_name):
    """
    Function to find the word that appeears most frequently in the text file.
    """
    content =  read_file(file_name)

    #Split the string into a list of words
    word_list = content.split()

    #Convert words to lowercase and remove punctuation
    word_list = [word_lower().strip('. , ! ? : ; () []') for word in word_list]

    #Use counter to count occurences of each word
    word_count = Counter(word_list)

    #Find the word tha appears most frequently
    most_frequent_word, occurrent_count = word_count.most_common(1)[0]

    return most_frequent_word, occurrent_count

#Path to the text file
file_name = 'example.txt'

#Call the function and print the result
most_frequent_word, occurrent_count = find_most_frequent_word(file_name)
print(f"The most frequent word is: '{most_frequent_word} with {occurrent_count} occurrences")


