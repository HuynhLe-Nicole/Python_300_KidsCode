# Write a program that splits a string into a list of words. Use the split() method

#Input a string 
input_str = "Hello world , welcome to the world of Python."
print("Original string:", input_str)

#Split the string into a list of words based on spaces
words_list = input_str.split()
print("List of words (split by space):", words_list)

#Splitting the String by Commas
#Split the string by commas
input_str_comma = "apple,banana,orange,grape"
print("Original string:", input_str_comma)

words_list_comma = input_str_comma.split(',')
print("List of words (split by commas):", words_list_comma)

#Splitting the String by Periods
#Split the string by periods
input_str_dot = "This.is.a.sample.sentence."
print("Original string:", input_str_dot)

words_list_dot = input_str_dot.split(',')
print("List of words (split by period):", words_list_dot)