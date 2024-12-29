# Write a program to add new mothods to the Student class. These new methods can provide any addtional functionality related to the student object, such as calculating age, updating the average grade, or displaying a greeting.
# Algorithm: 1_Add new method to the definition of Student class. 2_Update the class to utilize these new methods.

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
        
    #New method to update the average score
    def update_score(self, new_score):
        """Method to update the student's average score"""
        self.average_score = new_score
        print(f"New average score for student {self.name} is: {self.average_score}")

    #New method to display a greeting
    def greet(self):
        """Method to display a greeting from the student"""
        print(f"Hello! I am {self.name} and I am a senior. Nice to meet you!")

# Create a student object
student = Student("Nicole Le", 18, 9.3, "Jefferson County, Louisville City")

#Display student information
student.display_info()

#Classify the student
print(f"Classification: {student.classify()}")

#Update the average score and display information
student.update_score(9.8)

#Display greeting from the student
student.greet()