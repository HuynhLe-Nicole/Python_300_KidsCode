# Write a program that convert a list into a set
# Algorithm: 1_Initialize a list. 2_Convert the list into a set using the set() function

#Initialize the list
list1 = [1, 2, 3, 4, 5]
print("Initial list:", list1)

#Convert the list to a set
set1 = set(list1)
print("Set after conversion from list:", set1)

#Create an empty set and use a loop to add each element from the list into the set:
#Initialize an empty set
set1 = set()

#Iterate through each element of the list and add to the set
for item in list1:
    set1.add(item)