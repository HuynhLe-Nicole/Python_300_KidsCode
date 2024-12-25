# Write a program that finds the smallest element in a tuple without the min() function
#Algorithm: 1_Initialize a tuple with the desired elements. 2_Assume the first element is the smallest at the beginning. 3_Use for loop to iterate through each element in the tuple.
# 4_During each iteration, compare the current element with the smallest element found do far, and update the smallest element if the current element is smaller. 5_Print the smallest element.

#Initialize a tuple
my_tuple = (10, 20, 30, 40, 5, 50, 3, 25)

#Assume the first element is the smallest initally
min_element = my_tuple[0]

#Iterate through  each element in the tuple to find the samllest 
for element in my_tuple:
    if element < min_element:
        min_element = element

#Print the smallest element
print("The smallest element in the tuple is:", min_element)