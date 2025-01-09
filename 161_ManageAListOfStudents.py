# Write a program to manage a list of students using an object-oriented approach.
# Algorithm: 1_Create a Student class with attributes like name, age, and class. 2_Create a StudentManager class to manage the list of students. 3_Main method include: Add a new student to the list. Remove a student from the list. Display the list of students. 
# 4_Provide a use interface to enter commands and manage the list of students.

class Student:
    def __init__(self, name, age, class_name):
        self.name = name
        self.age = age
        self.class_name = class_name

    def _str_(self):
        return f"Student: {self.name}, Age: {self.age}, Class: {self.class_name}"
    
class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def remove_student(self, name):
        for student in self.student_list:
            if student.name == name:
                self.student_list.remove(student)
                return True
        return False
    
    def display_students(self):
        for student in self.student_list:
            print(student)


def menu():
        student_manager = StudentManager()
        while True:
            print("\n1. Add Student")
            print("2. Remove Student")
            print("3. Display Student List")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                class_name = input("Enter student class: ")
                student = Student(name, age, class_name)
                student_manager.add_student(student)
                print("Student added.")

            elif choice == '2': 
                name = input("Enter the name of the student to remove: ")
                if student_manager.remove_student(name):
                    print("Student removed.")
                else:
                    print("Student not found.")

            elif choice == '3':
                student_manager.display_students()

            elif choice == '4':
                print("Exiting the program.")
                break

            else: 
                print("Invalid choice, Please try again.")        


if __name__ == "_main_":
    menu()