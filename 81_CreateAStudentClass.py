# Wrtie a program to create a student class. This class will contain attributes and method to describe and manipulate student objects. The basic attributes of a student could include name, age, average score, and methods to display student information or calculate certain values.
# Algorithm: 1_Define the student class with basic attributes such as name, age, and average score. 2_Write the init method to initialize student objects with the defined attributes. 3_Write methods to manipulate the sudent object, such as displaying student information.

class Student:
    def _init_(self, name, age, average_score):
        """Constructor method to set the attributes of the student"""
        self.name = name
        self.age = age
        self.average_score = average_score

    def display_info(self):
        """Method to display the information of the student"""
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Score: {self.average_score}")

    def classify(self):
        """Method to classify the student based on  the average score"""
        if self.average_score >= 8.5:
            return "Excellent"
        elif self.average_score >= 6.5:
            return "Good"
        elif self.average_score >= 5.0:
            return "Average"
        else:
            return "Poor"

# Create a student object
student = Student("Nicole Le", 18, 9.3)

#Display student information
student.display_info()

#Classify the student
print(f"Classification: {student.classify()}")