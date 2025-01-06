# Write a program that uses the map() function to double elements in a given list.
# Algorithm: 1_Accept input as a list of number. 2_Define a function that doubles a number. 3_Use the map() function to apply the doubling function to each element in the list. 4_Output the result as a new list containing the doubled elements.

def double(n):
    """
    Function to double a number.
    """
    return n * 2

#Input list
numbers = [1, 2, 3, 4, 5]

#Use the map function to double the elements in the list
double_numbers = list(map(double, numbers))

print("List after doubling the elements:", double_numbers)