# Write a program that prints the first 10 happy numbers. Happy number is a natural number that will eventually reach 1 when replaced by the sum of squares of its digits. If not, it will enter an endless loop.
# Algorithm: 1_Write a function to check if a number is happy. 2_Use a loop to find and print the first 10 happy numbers.

def is_happy_number(n):
    """
    Function to check if a number is a happy number.
    """
    seen = set() #Initialize a set to keep track of numbers that have been encountered.

    while n != 1 and n not in seen: #Repeats the process of replacing until reaching 1 or encountering a number that was previously seen.

        seen.add(n) #Adds the current number to be set

        n = sum(int(char) ** 2 for char in str(n)) #Calculates the sum of squares of the digits of current number
        
    return n == 1 #Return True if the currrent number is 1, otherwise return False.


def first_n_happy_numbers(n):
    """
    Function to return a list of the first n happy numbers.
    """
    happy_numbers = [] #Initialize a list a store happy numbers.

    num = 1 #Starts checking from number 1

    while len(happy_numbers) < n: #Countinues the process until enough happy numbers are found

        if is_happy_number(num): #Check if the current number is happy

            happy_numbers.append(num) #Adds the happy number to the list

        num += 1 #Increments the current number by 1 to check the next number
    return happy_numbers

#Number of happy numbers to find
n = 10

#Call the function and print the result
happy_numbers = first_n_happy_numbers(n)
print("The first 10 happy numbers:", happy_numbers)