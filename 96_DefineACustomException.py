# Write a program that defines a custom exception. Create a new class to define own exception type by inheriting from the built-in Exception class.
# Algorithm: 1_Define a custom exception class that inherits from Exception. 2_Perform an action that may raise the custom exception inside a try block. 3_Catch the custom exception in an except block.

class CustomException(Exception):
    pass

def raise_custom_exception():
    try:
        raise CustomException("This is a custom exception!")
    except CustomException as e:
        print(e)

#Call the function to raise and catch the custom exception
raise_custom_exception()