# Write a program that joins words in a list into a single string.
# Algorithm: 1_Initialize a list of words. 2_Use the join method to concatenate the words in the list into a single string. 3_Print the resulting string.

#Method1: Using the join method

def join_words_to_striong(word_list):
    """
    Funtion to join words in a list into a string.
    """
    result_string = ' '.join(word_list)
    return result_string

#Initialize the list of words
word_list = ["This", "is", "a", "string", "of", "words"]

#Call the function and print the result
result_string = join_words_to_striong(word_list)
print(result_string)


#Method2 : Using a for loop to join words

def join_words_to_string(word_list):
    """
    Function to join words in a list into a string.
    """
    result_string = ""
    for word in word_list:
        result_string += word + " "
    result_string = result_string.strip() #Remove trailing whitespace at the end of the string
    return result_string

#Initilaze the list of words
word_list = ["This", "is", " a", "string", "of", "words"]

#Call the function and print the result
result_string = join_words_to_string(word_list)
print(result_string)