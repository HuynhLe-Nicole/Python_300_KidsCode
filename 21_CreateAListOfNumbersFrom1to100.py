# How to solve the problem
# 1. Using a loop (for loop) to add numbers one by one to a list
# 2. Or using Python's built-in function, range() and list() to create the list efficiently

# Create a list of number from 1 to 100
numbers = list(range(1, 101)) 
# range(1, 101): this function generates a sequencce of numbers. It starts at 1 and goes up to but does not include 101. So, it produces numbers from 1 to 100
# list(range(1, 101)): the range() function creates a sequence of numbers, but it's not a list yet. We use the list() function to convert this sequence into a list of numbers

# Print the list to the screen
print(numbers)

#Initialize an empty list
number = []
#Use a for loop to add numbers from 1 to 100 to the list
for i in range(1, 101): #Loop from 1 to 100
    numbers.append(i) #Add each number i to the list

#Print the list to the screen
print(numbers)
