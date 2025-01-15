# Write a program to create a simple decorator. A decorator is a function used to extend the functionality of another function without modifying its source code. It often handles logic both before and  after a function is executed.
# Algorithm: 1_Define the decorator. 2_Within the decorator, define an inner function that adds extra functionality to the original function.
# 3_Return the augmented function. 4_Apply the decorator to a specific function and verify the result.


def my_decorator(func): #Defines a decorator function named my_decorator that accepts a function func as a parameter
    def wrapper(): #Defines an inner function called warapper, which will replace the original function
        print("Something is happening before the function is called.")
        func() #calls the original function  passed to the decorator
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


#Calling the decorated function
say_hello()