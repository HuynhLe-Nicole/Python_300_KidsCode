# Write a program to manage class schedules using OOP. We will create basic objects  such as subjects, classes, and schedules.
# We will define corresponding classes to represent the properties and methods of each object, while also providing basic functions such as adding subjects, creating  classes, sorting schedules, and displaying class schedules.
# Algorithm: 1_Create a Subject class with attributes like subject name and subject code.
# 2_Create a Class class with attributes such as subjects, class time, and classroom.
# 3_Create a SchedulesManager class to manage the list of subjects and classes.
# 4_Key method: Adding a new subject. Creating a new class. Sorting the schedule. Displaying the schedule.
# 5_Provide a user interface to input commands and manage the class schedule


class Subject:
    def __init__(self, name, subject_code):
        self.name = name
        self.subject_code = subject_code

    def __str__(self):
        return f"Subject: {self.name}, Subject Code: {self.subject_code}"
    

class Class:
    def __init__(self, subject, class_time, classroom):
        self.subject = subject
        self.class_time = class_time
        self.classroom = classroom

    def __str__(self):
        return f"Class: {self.subject.name}, Time: {self.class_time}, Classroom: {self.classroom}"
    

class ScheduleManager:
    def __inti__(self):
        self.subject_list = []
        self.class_list = []

    def add_subject(self, subject):
        self.subject_list.append(subject)
        
    def create_class(self, subject_code, class_time, classroom):
        subject = self.find_subject(subject_code)
        if subject:
            classroom_instance = Class(subject, class_time, classroom)
            self.class_list.append(classroom_instance)
            return True
        return False
    
    def display_schedule(self):
        for classroom_instance in self.class_list:
            print(classroom_instance)

    def find_subject(self, subject_code):
        for subject in self.subject_list:
            if subject.subject_code == subject_code:
                return subject
        return None
    

def menu():
    schedule_manager = ScheduleManager()
    while True:
        print("\n1. Add Subject") 
        print("2. Create Class") 
        print("3. Display Schedule") 
        print("4. Exit") 
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter subject name: ")
            subject_code = input("Enter subject code: ")
            subject = Subject(name, subject_code)
            schedule_manager.add_subject(subject)
            print("Subject added.")

        elif choice == '2':
            subject_code = input("Enter subject code: ")
            class_time = input("Enter classs time: ")
            classroom = input("Enter classroom: ")
            if schedule_manager.create_class(subject_code, class_time, classroom):
                print("Class created.")
            else:
                print("Subject not found.")

        elif choice == '3':
            schedule_manager.display_schedule()

        elif  choice == '4':
            print("Exiting the program.")
            break 

        else:
            print("Invalid choice. Please choose again.")     