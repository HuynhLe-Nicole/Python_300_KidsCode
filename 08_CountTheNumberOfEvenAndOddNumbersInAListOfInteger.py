#Write a program to count the number of even and odd numbers in a list of integers.
#Algorithm: 1- Take a list of integer as input from the user. 2- Iterate throgh each number in the list and check if it is even or odd. 3- Count the number of even and odd numbers. 4_ Print the results.

#Program to count the number of even and odd numbers in a list
def count_even_odd(numbers):
    count_even = 0 #Initialize count for even numbers
    count_odd = 0 #Initialize count for odd numbers
    for number in numbers: #Loop through each number in the list
        if number % 2 == 0:  #Check if the number is even
            count_even += 1 #Increase even count by 1
        else:
            count_odd += 1 #Increase odd count by 1
    return count_even, count_odd  # Return the counts

#Get the list of integers from user input\
try:
    input_list = input("Enter integers separated by space: ") #Prompt user for input
    numbers = [int(num) for num in input_list.split()]  #Cover input string to a list of integers
    
    even_count, odd_count = count_even_odd(numbers)  #Call the counting function
    print(f"Number of even numbers: {even_count}")  # Display event count
    print(f"Number of odd numbers: {odd_count}") #Display odd count
except ValueError: #Handle the case where input is not valid integers
    print("Please enter valid integers.")