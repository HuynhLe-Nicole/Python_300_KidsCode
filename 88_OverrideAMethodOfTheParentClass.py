# Write a program that overrides a method in the parent class within the subclass and utilizes the method from the parent class within the subclass.
# Algorithm: 1_Define the base class Person with a method display_infor. 2_Define the subclass Student that inherits from the Person class. 3_Override the display_infor method in the Student class and use the parent class's method via the super() keyword. 4_Create an object from the Student class and call the display_infor method.

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
        #Use the parent class method to display name and age 
        super().display_infor()
        #Add information about class and average score\
        print(f"Class: {self.class_name}")
        print(f"Average Score: {self.average_score}")

#Create an object from the Student class
student = Student("Nicole Le", 18, "12A12", 9.3)

#Call the display_infor method of the Student object
student.display_infor()