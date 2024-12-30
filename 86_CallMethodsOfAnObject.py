# Write a program to call methods of an object.
# Algorithm: 1_Define the class Student with public and private methods. 2_Create an object from the Student class. 3_Call the public method of the object. 4_Call the private method of the object through the public method.

class Student:
    def _init_(self, name, age, average_score, address):
        """Constructor method to initialize the attributes of the student"""
        self.name = name 
        self.age = age 
        self.average_score = average_score 
        self.address = address 

    def display_info(self):
        """Public method to display the information of the student"""
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Score: {self.average_score}")
        print(f"Address: {self.address}")
        self._classify() #Call private method from public method

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
        
    def _classify(self):
        """Private method to classify the student based on the average score"""
        category = self.classify()
        print(f"Classification: {category}")

    
# Create student object
student = Student("Nicole Le", 18, 9.3, "Jefferson County, Louisville City")

# Call the public method of the object
student.display_info()

#Call the private method through the public method
#Note: Cannot call the private method directly from outside
# student._classify() #This would raise an AttributeError.