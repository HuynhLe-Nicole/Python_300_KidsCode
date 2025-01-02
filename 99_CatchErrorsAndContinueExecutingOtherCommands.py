# Write program that catches an error and then continues to execute other command.
# Algorithm: 1_Perform an action that may rise an exception within the try block. 2_Catch and handle the exception in the except block. 3_Execute a command after the try/except block.

def catch_error_continue():
    try:
        print("Trying to divide by zero...")
        result = 10 / 0
    except ZeroDivisionError  as e:
        print("Caught an exception:", e)

    print("This is a statement after the try/except block.")

catch_error_continue()