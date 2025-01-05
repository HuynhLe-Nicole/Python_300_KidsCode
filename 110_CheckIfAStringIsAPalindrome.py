# Write a program to check if a string is a palindrome. A palindrome is a string that reads the same forwards and backwards.
# Algorithm: 1_Accept input as a string. 2_Remove whitespaces and convert all characters to lowercase for accurate comparison. 3_Compare the string with its reversed version. 4_Return the result of check.

#Method1 : Using slicing

def check_palindrome(string):
    """
    Function to check if a string is a palindrome.
    """
    string = string.replace(" ", "").lower() #Remove whitespaces and convert to lowwercase
    return string == string[::-1] #Compare string with its reverse using slicing

#String to check
string1 = "A man a plan a canal Panama"
string2 = "Hello World"

#Call the function and print the results
print(check_palindrome(string1)) #True
print(check_palindrome(string2)) #False

#Method2 : Using a loop

def check_palindrome(string):
    """
    Function to check if a string is a palindrome.
    """
    string = string.replace(" ", "").lower()  #Remove whitespaces and convert to lowwercase
    n = len(string) #Get the length of the string
    for i in range(n//2): #Iterate through the first half of the string
    
        if string[i] != string[n - i - 1]: #Compare charaters at position i with its opposite character n - i - 1

            return False #If any characters do not match, return False
        
    return True #If all characters match, return True

#String to check
string1 = "A man a plan a canal Panama"
string2 = "Hello World"

#Call the function and print the results
print(check_palindrome(string1)) #True
print(check_palindrome(string2)) #Fasle