# Writing a personal information management program, using OOP to create basic object such as personal information and a manager for that information.
# We will create corresponding classes to represent the properties and methods of each object, while providing basic functions such as personal information, updating personal information, and displaying personal information.
# Algorithm: 1_Create a class PersonalInformation with attributes such as name, age, address, phone number, and email. 
# 2_Create a class PersonalInformationManager to manage the list of personal information.
# 3_Main methods: Adding new personal information. Updating personal information. Displaying personal information.
# 4_Provide a user interface to enter commands and manage personal information.


class PersonalInformation:
    def __init__(self, name, age, address, phone_number, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def update(self, name=None, age=None, address=None, phone_number=None, email=None):
        if name is not None: 
            self.name = name
        if age is not None: 
            self.age = age
        if address is not None: 
            self.address = address
        if phone_number is not None: 
            self.phone_number = phone_number
        if email is not None: 
            self.email = email

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Address: {self.address}, " 
                f"Phone Number: {self.phone_number}, Email: {self.email}")
    
class PersonalInformationManager:
    def __init__(self):
        self.information_list = []

    def add_information(self, info):
        self.information_list.append(info)

    def update_information(self, name, new_name=None, age=None, address=None, phone_number=None, email=None):
        for info in self.information_list:
            if info.name == name:
                info.update(new_name, age, address, phone_number, email)
                return True
        return False
    
    def display_information(self, name):
        for info in self.information_list:
            if info.name == name:
                print(info)
                return
        print("No personal information found.")


def menu():
    manager = PersonalInformationManager()
    while True:
        print("\n1. Add Personal Information")
        print("2. Update Personal Information")
        print("3. Display Personal Information")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            info = PersonalInformation(name, age, address, phone_number, email)
            manager.add_information(info)
            print("Peronal information has been added.")

        elif choice == '2':
            name = input("Enter the name of the personal information to update: ")
            new_name = input("Enter new name (or press Enter to keep unchanged): ")
            age = input("Enter new age (or press Enter to keep unchanged): ")
            address = input("Enter new address (or press Enter to keep unchanged): ")
            phone_number = input("Enter new phone number (or press Enter to keep unchanged): ")
            email = input("Enter new email (or press Enter to keep unchanged): ")
            age = int(age) if age else None 
            update_success = manager.update_information(name, new_name if new_name else None, age, address, phone_number, email)
            if update_success:
                print("Personal information has been updated.")
            else:
                print("No personal information found.")

        elif choice == '3':
            name = input("Enter the name of the personal information to display: ")
            manager.display_information(name)

        elif choice == '4':
            print("Exiting the program.")
            break 

        else:
            print("Invalid choice. Please try agian.")      
        