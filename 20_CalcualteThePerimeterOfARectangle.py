# Perimeter P = 2*(length + width)
# Area A = length * width
# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Get length and width from the user
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Check if the length and width are non-negative
    if length < 0 or width <  0:
        print("Length and width must be non-negative numbers.")
    else:
        # Calculate perimeter and area
        perimeter = rectangle_perimeter(length, width)
        area = rectangle_area(length, width)

        # Display the result
        print(f"The perimeter of the rectangle is: {perimeter}")
        print(f"The area of the rectangle is: {area}")
except ValueError:
    print("Please enter a valid number for length and width.") 
