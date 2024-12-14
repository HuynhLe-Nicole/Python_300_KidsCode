# The function that computes the power of a number. This mean that given a base (Ex:2) and an exponent(Ex:3), you want to calculate(2^3 = 8)
# Step to Solve the Problem: 
# 1. Input: enter base number (the number we want to rise) and an exponent (how many time we multiply the base).
# 2. Calculate the power: use a function to called power 
# 3. Output: show the result

# Function to calculate power of a number
def power(base, exponent):
    result = 1  # Start with 1 because anything to the power of 0 is 1
    for _ in range(abs(exponent)):  # Loop as many times as the absolute value of the exponent
        result *= base  # Multiply the result by the base each time
    if exponent < 0:
        result = 1 / result  # If exponent is negative, take the reciprocal
    return result  # Return the final result

# Input from the user
try:
    base = float(input("Enter the base: "))  # Get the base and convert to a float
    exponent = int(input("Enter the exponent: "))  # Get the exponent and convert to an integer
    print(f"{base} ^ {exponent} = {power(base, exponent)}")  # Show the result
except ValueError:
    print("Please enter a valid number for base and an integer for exponent.")

# Function power(base, exponent):
# Initialize a result variable to 1 
# Uses a loop to multiply the base by itself (the number of times is determined by the absolute value of the exponent).
#If the exponent is negative, it inverts the result (because raising a number to a negative exponent means taking the reciprocal)
