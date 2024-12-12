#Write a program to add an element to the end of a list. In Python, you can use the append() method of the list object to add an element to the end of a list
#Solution algorithm:
#1. Initialize the initial list.
#2. Enter the element to add from the user.
#3. Use the append() method to add the element to the end of the list.
#4. Print the list after adding the element.

# Initialize the initial list
my_list = [1, 2, 3, 4, 5]

#Enter the element to add
new_element = input("Enter the element to add to the list: ")

#Add the element to the end of the list
my_list.append(new_element)

#Print the list after adding the element
print("List after adding the element:", my_list)