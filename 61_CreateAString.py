# Write a program that creates a string

#Create a string
str1 = "Hello, World!"
print(str1)

#1.Using double or single quotes
str1 = "Hello, World!"
str2 = 'Hello, World!'

#2.Using triple quotes
str3 = """Hello, World!"""
str4 = '''Hello, World!'''

#3.Using the str() function
num = 123
str5 = str(num)  #'123'

#4.Concatenating strings: combine multiple strings using the + operator
str6 = "Hello, " + "World"

#5.Using f-strings
name = "World"
str7 = f"Hello, {name}!"

#6.Using the format() method
name = "World"
str8 = "Hello, {}!".format(name)