# Write a program to check if an element exist in a tuple.
# Algorithm: 1_Initialize a tuple with desired elements. 2_Ask the user to input the element they want to check. 3_Use the in operation to check if the element exists in the tuple. 4_Print the result of the check.

#Intialize a tuple
my_tuple = (10, 20, 30, 40, 50)

# Print the created tuple
print("Created tuple:", my_tuple)

#Ask for the element to check from the user
element = input("Enter the element to check: ")

#Convert the input element to the correspoding data type 
try: 
    # Try to convert the input element to an integer
    element = int(element)
except ValueError:
    try:
        #If it's not an integer, try to convert it to a float
        element = float(element)
    except ValueError:
        #If it's not a float , keep it as a string
        pass

#Check if the element exists in the tuple
if element in my_tuple:
    print(f"Element {element} exists in the tuple.")
else:
    print(f"Element {element} does not exist in the tuple.")