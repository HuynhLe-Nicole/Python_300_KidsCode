# Write a program to compute the Fibonacci sequence using two methods: iterative(for loop) and recursive
# Algorithm: Iterative method: 1_Create two variables to store the first two numbers of the Fibonacci sequence. 2_Use a loop to calculate subsequent Fibonacci numbers. 3_Store the Fibonacci numbers in a list and return that list.
# Recursive method: 1_Define a recursive function to compute the Fibonacci number at position n. 2_Call this recursive function to compute and print the Fibonacci sequence.

#Iterative method: Using for Loop

def fibonacci_for(n):
    """
    Function to compute the Fibonacci sequence using a for loop.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibo_seq = [0, 1]
    for i in range (2, n):
        next_fibo = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_fibo)

    return fibo_seq

#Number of Fibonacci elements to compute
n = 10

#Call the function and print the result
fibo_seq = fibonacci_for(n)

print ("Fibonacci sequence using for loop:", fibo_seq)

#Code Explanation: It check if n is less than or equal to 0 => return an empty list
#If n is 1 => return list containing only 0
#If n ia 2 => return the first two Fibonacci numbers, [0, 1]
#Then it uses a for loop to calculate the next Fibonacci numbers based on the sum of the last two numbers in the list and append them to the list.

#Recursive method

def fibonacci_recursive(n):
    """
    Recursive function to compute the Fibonacci number at position n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
def fibonacci_sequence_recursive(n):
    """
    Function to generate the Fibonacci sequence using recursion.
    """
    return [fibonacci_recursive(i) for i in range(n)]

#Number of Fibonacci elements to compute
n = 10

#Call the function and print the result
fibo_seq = fibonacci_sequence_recursive(n)
print("Fibonacci sequence using recursion:", fibo_seq)

#Code Explanation: Checks if n is less than  or equal to 0, return 0.
# If n is 1 -> return 1
# Calculates the Fibonacci number at position n by summing the Fibonacci numbers at positions n-1 and n-2