# Write a decorator that can return different functions based on certain conditions.
# Algorithm: 1_Define a decorator that accepts an argument. 2_Inside the decorator, define a wrapper function that takes the function to be decorated
# 3_In the wrapper function, check the argument and return the corresponding function. 4_Apply the decorator to the function that needs to be decorated.


def route(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if path == "/home" :
                return home(*args, **kwargs)
            elif path == "/about":
                return about(*args, **kwargs)
            else: 
                return func(*args, **kwargs)
        return wrapper
    return decorator

def home(name):
    return f"Welcome to the home page, {name}!"

def about(name):
    return f"This is the about page. Nice to meet you, {name}!"

@route("/home")
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))  #Output: Welcome to the home pagr, John!
            