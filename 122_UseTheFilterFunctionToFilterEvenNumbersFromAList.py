# Write a program that uses the filter() function to extract even numbers from a list.
# Algorithm: 1_Take input as a list of numbers. 2_Define a function to check if a number is even. 3_Use the filter() function to apply the checking function to each element of the list. 4_Ouput the result as a new list containing only the even numbers.

def is_even(n):
    """
    Function to check if a number is even.
    """
    return n % 2 == 0

#Input list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Use the filter function to filter even numbers from the list
even_numbers = list(filter(is_even, numbers))

print("List of even numbers:", even_numbers)
