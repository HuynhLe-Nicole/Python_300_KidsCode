# Write a program to calculate the distance between two points A and B in the Cartesian coordinate system.
# Algorithm: 1_Input the coordinates of points A and B. 2_Calculate the distance between points A and B using the Euclidean distance formula. 3_Output the distance. 

import math

def calculate_distance(point1, point2):
    return math.sqrt((poitn1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

pointA = (float(input("Enter x coordinate for point A: ")), float(input("Enter y coordinate for point A: ")))
pointB = (float(input("Enter x coordinate for point B: ")), float(input("Enter y coordinate for point B: ")))

distance = calculate_distance(pointA, pointB)
print(f"The distance between point A and point B is: {distance}")