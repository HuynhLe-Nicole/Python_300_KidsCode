# Write a program that concatenates two strings
#Algorithm: 1_Create two strings. 2_Concatenate the two strings together.

#Create two strings
str1 = "Hello, "
str2 = "World!"

#Concatenate the two strings
str3 = str1 + str2
print(str3)

#1. Using the join() method
#Create two strings
str1 = "Hello, "
str2 = "World!"

#Concatenate the two strings
str3 = ''.join([str1, str2])
print(str3)

#2. Using f-string
#Create two strings 
str1 = "Hello, "
str2 = "World!"

#Concatenate the two strings
str3 = f"{str1}{str2}"
print(str3)

#3. Using the format() method
#Create two strings
str1 = "Hello, "
str2 = "World!"

#Concatenate the two strings
str3 = "{}{}".format(str1, str2)
print(str3)