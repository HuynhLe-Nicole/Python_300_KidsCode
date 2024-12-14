#Write a program to remove an element from a list. In Python, you can use the remove() method of the list object to remove a specific element.
#Solution algorithm:
#1. Initialize an empty list.
#2. Enter the element to be removed from the user.
#3. Convert the input to the correct data type (integer or float).
#4. Check if the element exist in the list.
#5. If it exist, remove it using the remove() method.
#6. If it doesn't exist, print an error message.
#7. Print the updated list.

#Initialize an empty list
my_list = [1, 2, 3, 4, 5]

#Ask the user to input the element they want to remove
element_to_remove = input("Enter the element to remove: ")

#Covert the input to the correct data type
    #We convert the input to the correct data type using a try-except block. We first try to convert it to an integer using int(), and if that fails, we try to convert it to a float using float(). 
    #If both conversion fail, we keep it as a string.
try:
    # Try to convert to integer
    element_to_remove = int(element_to_remove)
except ValueError:
    try:
        #If not integer, try to convert to float
        element_to_remove = float(element_to_remove)
    except ValueError:
        #If not float, keep it as a string
        pass

# Check if the element exists in the list
if element_to_remove in my_list:
    #Remove the element if it exists
    my_list.remove(element_to_remove)
    print("Updated list:", my_list)
else:
    print("Element not found in the list.")