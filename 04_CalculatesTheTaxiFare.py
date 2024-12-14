#Write a program that calculates the taxi fare based on the distance traveled by the user. The fare is calculated accroding to different rates for different distances
#Assumptions:
# The first km is 10k VND
# From the second to tenth km, the fare is 8.5k VND per km.
# From eleventh km onwards, the fare is 7.5k VND per km.
#Algorithm:
#1. Take an input for the distance traveled by the user.
#2. Calculate the total fare based on the distance traveled using if-elif-else statements.
#3. Print the total fare.

# Define a function calculate_taxi_fare(km) that takes an integer km as input
def calculate_taxi_fare(km):
    #Calculate the total fare based on the distance traveled
    if km <= 1:
        fare = 10000
    elif km <= 10:
        fare = 10000 + (km - 1) * 8500
    else: 
        fare = 10000 + 9 * 8500 + (km - 10) * 7500
    return fare

#Take an input for the distance traveled by the user
try:
    distance = float(input("Enter the distance traveled: "))
    #Check if the input is a positive number
    if distance < 0 :
        print("Invalid distance. Please enter a postive number.")
    else:
        #Call the calculate_taxi_fare function with the input distance and print the result
        total_fare = calculate_taxi_fare(distance)
        print(f"The total taxi fare is: {total_fare} VND")
except ValueError:
    print("Please enter a valid number.")
    