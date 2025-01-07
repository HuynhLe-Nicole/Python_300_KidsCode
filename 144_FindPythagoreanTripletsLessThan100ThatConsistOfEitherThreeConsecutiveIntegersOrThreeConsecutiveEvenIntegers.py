# Write a program to find Pythagorean triplets less than 100 that consist of either three consecutive integers or three consecutive even integers. A Pythagorean triplet is a set of three positve integers a, b and c such that a^2 + b^2 = c^2
# Algorithm: 1_Check all sets of three consecutive integers or even numbers less than 100. 2_Verify if the triplet is a Pythagorean triplet. 3_If it is, add the triplet to the result list. 4_Print the results list.

def find_pythagorean_triplets():
    triplets = []
    for a in range(1, 98):
        b, c = a + 1, a + 2 # 3 consecutive numbers
        if a * a + b * b == c * c:
            triplets.append((a, b, c))
        b, c = a + 2, a + 4 # 3 consecutive even numbers
        if a * a + b * b == c * c:
            triplets.append((a, b, c))
    return triplets

print(find_pythagorean_triplets())


