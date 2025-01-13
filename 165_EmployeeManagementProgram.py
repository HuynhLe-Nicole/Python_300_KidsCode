# Write a program to manage employees using OOP. We will create corresponding classes to represent basic objects such as Employee, Department, and Human Resource Management. 
# We will implement such functionalities as adding employees, adding departments, assigning employees to departments, and displaying list of employees and departments.
# Algorithm: 1_Create an Employee class with attributes like name, age, position, and department. 2_Create Department class with attributes like name and a list of employess.
# 3_Create a HumanResourceManagement class to manage the list of employees and departments.
# 4_Main Method: 
# Adding a new employee to the system. 
# Adding a new department to the system.
# Assigning an employee to a department. 
# Displaying the list of employees. 
# Displaying the list of departments. 
# 5_Providing a user interface to input commands to manage employees and departments.

class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.department = None

    
    def __str__(self):
        department_name = self.department.name if self.department else "Not assigned"
        return f"Employee: {self.name}, Age: {self.age}, Position: {self.position}, Department: {department_name}"
    

class Department: 
    def __init__(self, name):
        self.name = name
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)
        employee.department = self

    def __str__(self):
        employees_str = ', '.join(emp.name for emp in self.employee_list)
        return f"Department: {self.name}, Employees: {employees_str}"


class HumanResourceManagement:
    def __init__(self):
        self.employee_list = []
        self.department_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def add_department(self, department):
        self.department_list.append(department)

    def assign_employee_to_department(self, employee_name, department_name):
        employee = self.find_employee(employee_name)
        department = self.find_department(department_name)
        if employee and department:
            department.add_employee(employee)
            return True
        return False
    
    def display_employee_list(self):
        for employee in self.employee_list:
            print(employee)


    def display_department_list(self):
        for department in self.employee_list:
            print(department)


    def find_employee(self, name):
        for employee in self.employee_list:
            if employee.name == name:
                return employee
        return None

    def find_department(self, name):
        for department in self.department_list:
            if department.name == name:
                return department
        return None
        

def menu():
    hr_management = HumanResourceManagement()
    while True:
        print("\n1. Add Employee")    
        print("2. Add Department")
        print("3. Assign Employee to Department")
        print("4. Display Employee List")
        print("5. Display Department List")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            position = input("Enter employee position: ")
            employee = Employee(name, age, position)
            hr_management.add_employee(employee)
            print("Employee added.")

        elif choice == '2':
            name = input("Enter department name: ")
            department = Department(name)
            hr_management.add_department(department)
            print("Department added.")

        elif choice == '3':
            employee_name = input("Enter employee name: ")
            department_name = input("Enter department name: ")
            if hr_management.assign_employee_to_department(employee_name, department_name):
                print("Employee assigned to department.")
            else:
                print("Could not assign employee to department.")

        
        elif choice == '4':
            hr_management.display_employee_list()

        elif choice == '5':
            hr_management.display_department_list()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select again.")