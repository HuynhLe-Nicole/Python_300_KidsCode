# Write a program to create a decorator that can measure the execution time of a function. This decorator will track the time from the moment the function starts until it finished and print out the execution time.
# Algorithm: 1_Define a decorator to measure the execution time of a function. 2_Inside the decorator, define a nested function to handle the timing. 3_Use the time module to capture the start and end times of the function execution.
# 4_Return the decorated function with the added timing functionality. 5_Apply the decorator to a specifc function and test the result.


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  #Get the start time
        result = func(*args, **kwargs)  #Call the original function
        end_time = time.time()  #Get the end time
        execution_time = end_time - start_time  #Calculate execution time
        print(f"Function {func.__name__} took {execution_time:.6f} seconds to execute")
        return result
    return wrapper


@timing_decorator
def example_function():
    time.sleep(2)  # Simulate a time-consuming task
    return "Function execution complete"


#Calling the decorated function
print(example_function())