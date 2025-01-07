# Write a program that computes the sum, difference, product, and quotient of tow fractions.
# Algorithm: 1_Define a class Fraction with two attributes: numerator(the top part) and denominator(the bottom part). 2_Define methods for adding, subtracting, multiplying, and dividing two fractions. 
#3_Simplify the fractions when performing operations. 4_Print the results.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return f"{numerator // gcd(numerator, denominator)} / {denominator // gcd(numerator, denominator)}"
    
    def subtract(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return f"{numerator // gcd(numerator, denominator)} / {denominator // gcd(numerator, denominator)}"
    
    def multiply(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return f"{numerator // gcd(numerator, denominator)} / {denominator // gcd(numerator, denominator)}"
    
    def divide(self, other):
        numerator = self.numerator * other.denominator 
        denominator = self.denominator * other.numerator 
        return f"{numerator // gcd(numerator, denominator)} / {denominator // gcd(numerator, denominator)}"
    
#Test
frac1 = MyFraction(1, 2)
frac2 = MyFraction(2, 3)

print(f"Sum: {frac1.add(frac2)}")
print(f"Difference: {frac1.subtract(frac2)}")
print(f"Product: {frac1.multiply(frac2)}")
print(f"Quotient: {frac1.divide(frac2)}")
    
    