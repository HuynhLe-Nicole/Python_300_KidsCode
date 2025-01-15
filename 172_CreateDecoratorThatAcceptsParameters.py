# Write a program to create a decorator that can accept parameters. This decorator will not only add functionality to the function but also change the behavior of the function beased on the arguments provided to the decorator.
# Algorithm: 1_Define a main decorator that can accept parameters. 2_Inside the main deocrator, define a nested decorator to enhance the original function.
# 3_In the nested decorator, define an inner function to perform the additional functionality. 4_Return the decorated function. 5_Apply the parameterized decorator to a specific function and check the result.


def repeat(n): #Defines a main decorator function named repeat that takes on parameter n
   
    def decorator(func): #Defines a nested decorator that takes a function func to be decorated
        
        def wrapper(*args, **kwargs): #Defines an inner functiokn named wrapper that accpets any number of positional and keyword arguments.
            
            for _ in range(n): #Loops n times
            
                func(*args, **kwargs) #Calls the original function func with its arguments.

        return wrapper
    
    return decorator

@repeat(3) # Uses the repeat decorator with the argument 3 to decorate the say_hello function
def say_hello(): 
    
    print("Hello!")


#Calling the decorated function
say_hello()

# Creating a parameterized decorator without using a loop
def multiply_by(factor):
    def multiply_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * factor
        return wrapper
    return multiply_decorator

@multiply_by(2)
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 4)) # Output: 14