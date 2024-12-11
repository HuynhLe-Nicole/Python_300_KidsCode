# Circumference C = 2*pi*r 
#  Ares A = pi*r^2
import math # This imports the math library that allows us to use pi and other math function

# Function to calculate the circumference of  a circle
def circumference(radius):
    return 2 * math.pi * radius # Uses the formula C = 2*pi*r

# Function to calculate the area of a circle
def area(radius):
    return math.pi * radius * radius # Use the formula A= pi*r^2

# Get the radius from the user
try: 
    radius = float(input("Enter the radius of the circle: ")) # Covert user input to a float
    if radius < 0: # Check if the input is negative
        print("Radius must be a non-negative number.")
    else: 
        circ = circumference(radius) # Call the circumference function
        ar = area(radius) # Call the area function

        # Display the results
        print(f"The circumference fo the circle is: {circ}")
        print(f"The area of the circle is: {ar}")
except ValueError: # Handle the case where input is not valid float
    print("Please enter a vaild number for the radius.")