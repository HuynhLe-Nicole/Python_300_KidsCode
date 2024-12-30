# Write a program to access and modify the values of the properties of an object. Both public and private properties need to be handled.
#Algorithm: 1_Define the Student class with public and private properites. 2_Create an object from the Student class. 3_Access and modify the values of public properties directly. 3_Access and modify the values of private properties using getter and setter  methods.

class Student:
    def _init_(self, name, age, average_score, address):
        """Initialization method to set the student's properties"""
        self.name = name #Public properties
        self._age = age #Private properties(single underscore indicates this is intended to be private)
        self.average_score = average_score #Public properties
        self._address = address #Private properties

    def display_info(self):
        """Method to display the information of the student"""
        print(f"Student: {self.name}")
        print(f"Age: {self._age}")
        print(f"Average Score: {self.average_score}")
        print(f"Address: {self._address}")

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
        

    #Getter for the private property _age
    @property
    def age(self):
        return self._age
    
    #Setter for the private property _age
    @age.setter
    def age(self, new_age):
        if new_age > 0: 
            self._age = new_age
        else:
            print("Invalid age!")

    #Getter for the private property _address
    def get_address(self):
        return self._address
    
    #Setter for the private property _address
    def set_address(self, new_address):
        self._address = new_address

# Create a student object
student = Student("Nicole Le", 18, 9.3, "Jefferson County, Louisville City")

#Access and modify public properties
print(f"Before change: Name - {student.name}, Average Score - {student.average_score}")
student.name = "Leo Le"
student.average_score = 8.9
print(f"After change: Name - {student.name}, Average Score - {student.average_score}")

#Access and modify private properties via getter and setter
print(f"Before change: Age - {student.age}, Address - {student.get_address()}")
student.age = 18
student.set_address("Harris County, Houston City")
print(f"After change: Age - {student.age}, Address - {student.get_address()}")

#Display student information
student.display_info()