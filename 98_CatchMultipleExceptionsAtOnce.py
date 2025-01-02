# Write a program to catch multiple exceptions stimultaneously. Use multiple except blocks to catch and handle different types of exceptions.

def catch_multiple_exceptions(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    except TypeError as e:
        print("Caught an exception:", e)


catch_multiple_exceptions(10, 0)
catch_multiple_exceptions(10, "zero")
