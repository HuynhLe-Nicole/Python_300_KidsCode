# Write a program that joins words from a list into a single string. Use the join() method of strings

#Input a list of words
words_list = ["Hello", "world", "welcome", "to", "Python"]
print("List of the words:", words_list)

#Join the words into a string with a space as the separator
joined_str = ' '.join(words_list)
print("String after joining:", joined_str)

#Joining the Words with Commas
#Join the words with a comma
joined_str_comma = ', '.join(words_list)
print("String after joining with commas:", joined_str_comma)

#Joining the Words with Semicolons
#Join the words with a semicolon
joined_str_semicolon = '; '.join(words_list)
print("String after joining with semicolons:", joined_str_semicolon)