# Write a program to create a decorator that can call a function multiple times. This decorator will accept an argument to specify the number of times the function should be called and then execute that function the specified number of times.
# Algorithm: 1_Define a decorator to call a function multiple times. 2_Inside the decorator, define an inner function to perform the multiples calls
# 3_Return the enhanced function. 4_Apply the decorator to a specific function and check the results.


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hello():
    print("Hello!")


# Calling the decorated function
say_hello()