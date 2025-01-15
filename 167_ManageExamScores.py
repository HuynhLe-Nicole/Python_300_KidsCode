# Write a program that manages student's exam scores for each examination using OOP. We will create basic  objects such as students, subjects, exams, and score management. 
# Specific classes will represent the properties and methods of each object, and we will provide basic functions such as adding students, adding subjects, adding exams, recording scores, and displaying student's scores for each examination.
# Algorithm: 1_Create a Student class with attributes such as name and student ID.
# 2_Create a Subject class with attributes like subject name and subject code.
# 3_Create an Exam class with attributes like exam name and exam code.
# 4_Create a Score class to store the exam score for each student for each subject in each exam.
# 5_Create a ScoreManager class to manage the lists of students, subjects, exams, and scores.
# 6_Main methods: Adding a new student. Adding a new subject. Adding a new exam. Recording exam scores. Displaying each student's exam scores.
# 7_Provide a user interface to enter commands and manage exam scores.


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, Student ID: {self.student_id}"
    

class Subject:
    def __init__(self, name, subject_code):
        self.name = name
        self.subject_code = subject_code

    def __str__(self):
        return f"Subject: {self.name}, Subject Code: {self.subject_code}"


class Exam:
    def __init__(self, name, exam_code):
        self.name = name
        self.exam_code = exam_code

    def __str__(self):
        return f"Exam: {self.name}, Exam Code: {self.exam_code}"


class Score:
    def __init__(self, student, subject, exam, score):
        self.student = student
        self.subject = subject
        self.exam = exam
        self.score = score

    def __str__(self):
        return f"Student: {self.student.name}, Subject: {self.subject.name}, Exam: {self.exam.name}, Score: {self.score}"


class ScoreManager:
    def __init__(self):
        self.student_list = []
        self.subject_list = []  
        self.exam_list = []  
        self.score_list = []                

    def add_student(self, student):
        self.student_list.append(student)

    def add_subject(self, subject):
        self.subject_list.append(subject)

    def add_exam(self, exam):
        self.exam_list.append(exam)

    
    def record_score(self, student_id, subject_code, exam_code, score):
        student = self.find_student(student_id)
        subject = self.find_subject(subject_code)
        exam = self.find_exam(exam_code)
        if student and subject and exam:
            score_record = Score(student, subject, exam, score)
            self.score_list.append(score_record)
            return True
        return False
    
    def display_scores(self, student_id):
        student = self.find_student(student_id)
        if student:
            for score_record in self.score_list:
                if score_record.student == student:
                    print(score_record)

        else: 
            print("Student not found.")

    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student
        return None
    
    def find_subject(self, subject_id):
        for subject in self.subject_list:
            if subject.subject_id == subject_id:
                return subject
        return None
    
    def find_exam(self, exam_id):
        for exam in self.exam_list:
            if exam.exam_id == exam_id:
                return exam
        return None
    

def menu():
    sm = ScoreManager()
    while True:
        print("\n1. Add Student")
        print("2. Add Subject")
        print("3. Add Exam")
        print("4. Record Exam Score")
        print("5. Display Student's Exam Scores")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            sm.add_student(student)
            print("Student added.")

        elif choice == '2':
            name = input("Enter subject name: ")
            subject_id = input("Enter subject ID: ")
            subject = Subject(name, subject_id)
            sm.add_subject(subject)
            print("Subject added.")

        elif choice == '3':
            name = input("Enter exam name: ")
            exam_id = input("Enter exam ID: ")
            exam = Exam(name, exam_id)
            sm.add_exam(exam)
            print("Exam added.")

        elif choice == '4':
            subject_id = input("Enter subject ID: ")
            student_id = input("Enter student ID: ")
            exam_id = input("Enter exam ID: ")
            score = float(input("Enter exam score: "))
            if sm.record_score(student_id, subject_id, exam_id, score):
                print("Score recorded.")
            else:
                print("Cannot record score (student, subject, or exam not found).")

        elif choice == '5':
            student_id = input("Enter student ID: ")
            sm.display_scores(student_id)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose again.")

    
    