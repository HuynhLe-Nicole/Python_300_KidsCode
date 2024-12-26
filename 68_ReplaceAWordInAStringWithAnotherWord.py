# Write a program to replace a specific word in a string with another word. Use the replace() method of strings
# Algorithm: 1_Input a string. 2_Input the word to replace. 3_Input the replacement word. 4_Use the replace() method to replace the word in the string. 5_Print the modified string.

#Input a string 
input_str = "Hello world, welcome to the world of Python."
print("Original string:", input_str)

#Input the word to replace
word_to_replace = "world"
print("Word to replace:", word_to_replace)

#Input the replacement word
replacement_word = "universe"
print("Replacement word:", replacement_word)

#Replace the word in the string
new_str = input_str.replace(word_to_replace, replacement_word)
print("String after replacement:", new_str)