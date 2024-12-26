#Write a program to check if a specific word is contained within a string.

#Create a string and a word to check
str1 = "Hello, World!"
word = "World"

#Check if the string contains the word
contains_word = word in str1
print(contains_word)

#Use the find() method of the string to check if the word exists in the string
#Create a string and a word to check
str1 = "Hello, World!"
word = "World"

#Check if the string contains the word
contains_word = str1.find(word) != -1
print(contains_word)