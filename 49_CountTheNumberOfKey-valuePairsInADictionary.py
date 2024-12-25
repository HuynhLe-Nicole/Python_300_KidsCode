# Write a program to count the number of key-value pairs in a dictionary and list various methods to count them.
# Algorithm: 1_Use the len() function directly on dictionary. 2_Use the items() method along with the len() function. 3_Use a for loop to count manually.

#Initialize a dictionary with some initial key-value pairs
my_dict ={
    'name' : 'Alice', 
    'age' : 25,
    'city' : 'New York'
}

#Print the initial dictionary 
print("Initial Dictionary:", my_dict)

#Method 1: Use the len() function directly on the dictionary
count1 = len(my_dict)
print("Number of key-value pairs (Method 1):", count1)

#Method 2: Use the items() method and the len() function
count2 = len(my_dict.items())
print("Number of key-value pairs (Method 2):", count2)

#Method 3: Use a for loop to count manually
count3 = 0
for _ in my_dict:
    count3 += 1
print("Number of key-value pairs (Method 3):", count3)