# Write a program that catches multiple types of errors and then raises them to another function to log the errors into a file. Use the raise keyword to throw an exception, which can then be caught and handled elsewhere.

def throw_error():
    try:
        result = 10 / 0  #This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        raise e  #Raising the caught exception
    except TypeError as e:
        raise e  #Raising the caught exception
    
def log_error():
    try:
        throw_error()  #Attempting to execute the function that may throw an error
    except Exception as e:
        with open('error.txt', 'a') as f: #Open the error log file in append mode
            f.write(e) + '\n'  #Log the error message
log_error()  #Call the function to catch errors and log them.