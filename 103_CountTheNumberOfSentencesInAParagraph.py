# Write a program that counts the number of sentences in a paragraph.
# Algorithm: 1_Accept the paragraph input from the user or define a preset paragraph. 2_Use punctuation characters to split the paragraph into sentences.
# 3_Count the number of sentences obtained after the split. 4_Print the result.


#Method1: Using re.split() with multiple punctuation marks

import re

def count_sentences_1(paragraph):
    """
    This function uses regex to split the paragraph into sentences and count the number of sentences.
    """

    #Use regex to split the paragraph into sentences
    sentences = re.split('r[.?!]', paragraph)

    #Remove empty elements
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

#Get paragraph input from the user
paragraph = input("Enter a paragraph: ")

# Call the function and print the result
sentence_count = count_sentences_1(paragraph)
print(f"The number of sentences in the paragraph (method 1) is: {sentence_count}")

#Method2: Iterating through each characters and counting punctuation

def count_sentences_2(paragraph):
    """
    This function iterates through each characters in the paragraph and counts puctuation marks to determine the number of sentences.
    """

    sentence_count = 0
    puctuation_marks = {'.', '?', '!'}

    for char in paragraph:
        if char  in puctuation_marks:
            sentence_count += 1
    
    return sentence_count

#Call the function and print the result
sentence_count = count_sentences_2(paragraph)
print(f"The number of sentences in the paragraph (method 2) is: {sentence_count}")