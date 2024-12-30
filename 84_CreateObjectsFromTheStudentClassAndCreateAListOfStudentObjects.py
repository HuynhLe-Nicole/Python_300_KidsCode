# Write a program to create objects from the Student class and create a list od Student objects. This will help manage information of multiple students at the same time.
# Algorithm: 1_Define the Student class with the necessary attributes and methods. 2_Create instances(objects) of the Student class. 3_Create a list to hold the Student objects. 4_Display the information of each object in the list.

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
        

# Create student objects
student1 = Student("Nicole Le", 18, 9.3, "Jefferson County, Louisville City")
student2 = Student("Leo Le", 16, 9.1, "Harris County, Houston City")
student3 = Student("Hao Le", 19, 8.3, "Jefferson County, Louisville City")

#Create a list of student objects
students_list = [student1, student2, student3]

#Display information of each student in the list
for  student in students_list:
    student.display_info()
    print(f"Classification: {student.classify()}")
    print("-----")