# Write a program to create a decorator that can modify the return value of a function.
# Algorithm: 1_Define a decorator to modify the return value of a function. 2_Inside the decorator, define a nested function to perform the modification of the return value. 
# 3_Return the decorated function with the enhanced functionality. 4_Apply the decorator to a specific function and test the result.


def modify_return_value_decorator(func):
    def wrapper (*args, **kwargs):
        # Call the original function and get the return value
        result = func(*args, **kwargs)
        # Modify the return value
        modified_result = result * 2 #EX: double the return value
        return modified_result
    return wrapper


@modify_return_value_decorator
def get_number():
    return 5


# Calling the decorated function
print(get_number())