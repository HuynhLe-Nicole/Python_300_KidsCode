# Wrtie a program to add a new properties to the Student class. This new property could be any additional information about the student , such as address, class, or phone number. We will add the address property to the student  and adjust the method to display and handle this new property.

# Algorithm: 1_Update the Student class to include a new property. 2_Update the _init_ method to accept and initialize the value for the new property. 3_Update the existing methods(such as display_info) to show the new property information.
class Student:
    def _init_(self, name, age, average_score, address):
        """Initialization method to set the student's properties"""
        self.name = name
        self.age = age
        self.average_score = average_score
        self.address = address

    def display_info(self):
        """Method to display the information of the student"""
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Score: {self.average_score}")
        print(f"Address: {self.address}")

    def classify(self):
        """Method to classify the student based on the average score"""
        if self.average_score >= 8.5:
            return "Excellent"
        elif self.average_score >= 6.5:
            return "Good"
        elif self.average_score >= 5.0:
            return "Average"
        else:
            return "Poor"

# Create a student object
student = Student("Nicole Le", 18, 9.3, "Jefferson County, Louisville City")

#Display student information
student.display_info()

#Classify the student
print(f"Classification: {student.classify()}")