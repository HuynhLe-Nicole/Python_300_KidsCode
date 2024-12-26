# Write a program to convert a string to lowercase

#Create a string
str1 = "Hello, World!"

#Convert the string to lowercase
lowercase_str = str1.lower()
print(lowercase_str)

#Use a for loop and the ord() function 
#Create a string
str1 = "Hello, World!"

#Convert the string to lowercase
lowercase_str = ""
for char in str1:
    if 'A' <= char <= 'Z':
        lowercase_str += chr(ord(char) + 32)
    else:
        lowercase_str += char
print(lowercase_str)