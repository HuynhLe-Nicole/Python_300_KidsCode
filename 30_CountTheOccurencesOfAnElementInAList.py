# Write a program to count how many times a specific element appears in a list.
# Algorithm: 1_Initialize the initial list. 2_Take the element to count from user input. 3_Use the count() method to find the number of occurences of the element in the list. 4_Print the number of occurrences of the element.

# Initialize the initial list
my_list = [1, 3, 7, 8, 7, 5, 6, 7, 2, 7, 10]

#Print the initial list 
print("Initial list:", my_list)

#Input the element to count occurrences from the user
element_to_count = input("Enter the element to count occurrences: ")

#Covert the input element from the user to the appropriate data type
try:
    #Attempt to covert the input  element to an integer
    element_to_count = int(element_to_count)
except ValueError:
    try:
        #If not an integer, attempt to convert it to a float
        element_to_count = float(element_to_count)
    except ValueError:
        #If not a float, keep it as a string
        pass

#Count the occurrences of the element in the list
count = my_list.count(element_to_count)

#Print the number of occurrences of the element
print(f"The element {element_to_count} appears {count} times in the list.")