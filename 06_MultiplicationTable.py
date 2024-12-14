#Write a program to print the multiplication table from 1 to 10. The multiplication table shows the results of multiplying each number from 1 to 10 by the nnumbers from 1 to 10
#Algorithm:
#1. There is no user input required.
#2. Output the multiplication table from 1 to 10.
#3. Use nested loops o iterate through numbers from 1 to 10:
    #The outer loop will iterate over numbers representing the multiplican (the number being multiplied).
    #The inner loop will iterate over numbers representing the multiplier (the number that multiplies the multiplicand).
#4. Print the result of the multiplication for each pair.

#Program to print the multiplication table from 1 to 10
def print_multiplication_table():
    for i in range (1,11): #Outer loop for the multiplicand
        print(f"Multiplication table for {i}:")
        for j in range(1,11): #Inner loop for the multiplier
            print(f"{i}*{j} = {i*j}") #Print the result of the multiplication
        print() #Print an empty line to separate the multiplication tables

#Call the function to print the multiplication table
print_multiplication_table