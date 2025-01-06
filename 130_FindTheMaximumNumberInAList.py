# Write a program using a lambda function to find the maximum number in a list.
# Algorithm: 1_Use the max() function to find maximum number in the list, specifying  a lambda function as the key. 2_Print the maximum number.

#List to find the maximum number
numbers = [1, 2, 3, 4, 5]

#Find the maxinmum number in the list
max_number = max(numbers, key=lambda x: x)

#Alternative method: Using a Loop
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num

print(f"The maximum number in the list: {max_number}")