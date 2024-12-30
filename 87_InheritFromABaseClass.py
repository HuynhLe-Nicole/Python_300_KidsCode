# Write a program that inherit from a base class.
#Algorithm: 1_Define the base class Person. 2_Define the subclass Student that inherits from the Person class. 3_Add specific attributes and methods to the Student class. 4_Create an object from the Student class and call methods from both the base and derived class.

#Define the base class Person
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_infor(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

#Define the Student class that inherits from the Person class
class Student(Person):
    def _init_(self, name, age, class_name, average_score):
        supre()._init_(name, age)
        self.class_name = class_name
        self.average_score = average_score

    def display_infor(self):
        super().display_infor()
        print(f"Class: {self.class_name}")
        print(f"Average Score: {self.average_score}")
        

    def classify(self):
        """Public method to classify the student based on the average score"""
        if self.average_score >= 8.5:
            return "Excellent"
        elif self.average_score >= 6.5:
            return "Good"
        elif self.average_score >= 5.0:
            return "Average"
        else:
            return "Poor"
        
#Create an object from the Student class
student = Student("Nicole Le", 18, "12A12", 9.3)

#Call methods
student.display_infor()
print(f"Classification: {student.classify()}")