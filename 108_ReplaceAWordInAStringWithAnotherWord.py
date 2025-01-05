# Write a program that replaces one word in a string with another word.
# Algorithm: 1_Receive the initial string, the word to be replaced, and the replacement word as input. 2_Use the replace method to substitute the word in the string. 3_Print the resulting string.

#Method1: Using the replace method

def replace_word(string, old_word, new_word):
    """
    Function to replace a word in a string with another word.
    """
    result_string = string.replace(old_word, new_word)
    return result_string

# Initial string 
initial_string = "This is an example of a string."

# Word to replace and replacement word
old_word = "example"
new_word = "demo"

# Call the function and print the result
result_string = replace_word(initial_string, old_word, new_word)
print(result_string)

#Method2: Using regular expression  with re.sub

def replace_word(string, old_word, new_word):
    """
    Function to replace a word in a string with another word.
    """
    result_string = string.replace(old_word, new_word)
    return result_string

#Initial string 
initial_string = "This is an example of a string."

#Word to replace and replacement word
old_word = "example"
new_word = "demo"

#Call the function and print the result
result_string = replace_word(initial_string, )