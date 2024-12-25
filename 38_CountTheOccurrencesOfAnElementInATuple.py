# Write a program that counts how many times an element appears in a tuple.
# Algorithm: 1_Initialize a tuple with the desired elements. 2_Ask the user to input the element they want to count. 3_Use the count() method to count how many times the element appears in the tuple. 4_Print the count result.

# Initialize a tuple 
my_tuple = (10, 20, 30, 20, 40, 50, 20, 60)

#Print the created tuple
print("Created tuple:", my_tuple)

#Ask for the element to count from the user
element = input("Enter the element to count occurrences: ")

#Convert the input element to the corresponding data type 
try:
    #Try to convert the input element to an integer
    element = int(element)
except ValueError:
    try:
        #If it's not an integer, try to convert it to a float
        element = float(element)
    except ValueError:
        #If it's not a float, keep it as a string
        pass

# Count the occurrences of the element in the tuple
count = my_tuple.count(element)

#Print the number of occurrences of the element
print(f"The element  {element} apprears {count} times in the tuple.")