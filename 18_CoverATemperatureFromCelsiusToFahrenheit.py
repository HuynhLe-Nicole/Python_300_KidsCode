# Write a function that coverts a temperature from Celsius to Fahrenheit. The formula: F = (C * 9/5) +32
# Steps to solve the problem
# 1. Get Celsius temperature from the users
# 2. Use the function to calculate the Fahrenheit
# 3. Print the result 

def celsius_to_fahrenheit(celsius):
    #Apply the coversion formula
    return celsius * 9 / 5 + 32

# Prompt user to enter temperature in Celsius
try: 
    celsius = float(input("Enter temperature in Celsius: ")) # Get input and covert to float
    fahrenheit = celsius_to_fahrenheit(celsius) # Call the function to covert
    print(f"{celsius}°C is equal to {fahrenheit}°F") # Display the result
except ValueError:
    print("Please enter a valid number for Celsius.") # Handle invalid input