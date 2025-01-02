# Write a program to count the number of characters in a string. 
#Algorithm: Method1: Using the len() function: Use the len() function to count the number of characters in the string. 
#Method2: Iterate through each character and count: Use a loop to iterate through each character in the string and increment a counter

#Method1: Using the len() function
def count_characters_1(string):
    """
    This function uses the len() function to count the number of characters in a string 
    """
    return len(string)

#Get the string input from the user
string = input("Enter s string: ")

#Call the function and print the result
character_count = count_characters_1(string)
print(f"The number of characters in the string (method1) is: {character_count}")

#Method2: Iterate through each character and count
def count_characters_2(string):
    """
    This function uses a loop to count the number of characters in a string.
    """
    count = 0
    for character in string:
        count += 1
    return count

#Call the function and print the result
character_count = count_characters_2(string)
print(f"The number of characters in the string (method2) is: {character_count}")