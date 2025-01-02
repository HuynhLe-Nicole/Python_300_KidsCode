# Write a program that utilizes the try-except-finally block. This block is used to catch and handle exceptions, as well as to ensure that certain actions are executed, regardless of whether an exception occurs or not.\
# Algorithm: 1_Perform an action that may cause an exception within the try block. 2_Catch and handle the exception in the except block. 3_Perform an action in the finally block.

def try_except_finally():
    try:
        print("Trying to divide by zero...")
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    finally:
        print("This is the finally block.")

try_except_finally()