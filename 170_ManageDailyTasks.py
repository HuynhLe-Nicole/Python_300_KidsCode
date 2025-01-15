# Writing a program to manage daily tasks. It allow users to add, edit, delete, and display tasks for specific day.
# Algorithm: 1_Create a Task class with attributes such as name, description, and status(completed/incomple).
# 2_Create a TaskManager class to manage the list of tasks. 
# 3_The main methods: Adding a new task. Editing an existing task. Deleting a task. Displaying the task list.
# 4_Provide a user interface to enter commands and manage daily tasks.


class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def update(self, name=None, description=None, completed=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if completed is not None:
            self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task Name: {self.name}, Description: {self.description}, Status: {status}"

class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def update_task(self, name, new_name=None, description=None, completed=None):
        for task in self.task_list:
            if task.name == name:
                task.update(new_name, description, completed)
                return True
        return False

    def delete_task(self, name):
        for task in self.task_list:
            if task.name == name:
                self.task_list.remove(task)
                return True
        return False

    def display_task_list(self):
        if not self.task_list:
            print("No tasks available.")
        else:
            for task in self.task_list:
                print(task)

def memu():
    task_manager = TaskManager()
    while True:
        print("\n1. Add a new task")
        print("2. Edit a task")
        print("3. Delete a task")
        print("4. Display task list")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task = Task(name, description)
            task_manager.add_task(task)
            print("New task has been added.")

        elif choice == '2':
            name = input("Enter the name of the task to edit: ")
            new_name = input("Enter ne name (or press Enter to keep it unchanged): ")
            new_description = input("Enter new description (or press Enter to keep it unchanged): ")
            completed = input("Is the task completed? (yes/no): ")
            completed = True if completed.lower() == "yes" else False
            update_success = task_manager.update_task(name, new_name if new_name else None, new_description if new_description else None, completed)
            if update_success:
                print("Task has been updated.")
            else:
                print("Task not found.")

        elif choice == '3':
            name = input("Enter the name of the task to delete: ")
            delete_success = task_manager.delete_task(name)
            if delete_success:
                print("Task has been deleted.")
            else:
                print("Task not found.")

        elif choice == '4':
            print("Task list:")
            task_manager.display_task_list()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

            