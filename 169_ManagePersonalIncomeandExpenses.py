# Write a program to manage personal income and expenses on a monthly basic. Using OOP to create basic objects such as transactions(income/expenses) and a management system for income and expenses.
# Algorithm: 1_Create a Transaction class with attributes such as amount, type(income/expenses), and description.
# 2_Create a Month class to represent the income and expenses for each month.
# 3_ Create a IncomeExpeneseManager class to manage the list of months and transactions.
# 4_The main methods: Adding a new transaction for each month. Displaying the income and expenses information for each month. Providing a user interface to enter commands and manage income and expenses.

class Transaction: 
    def __init__(self, amount, transaction_type, description):
        self.amount = amount
        self.transaction_type = transaction_type
        self_description = description

    def __str__(self):
        return f"Amount: {self.amount}, Type: {self.transaction_type}, Description: {self.description}"
    
class Month:
    def __init__(self, month):
        self.month = month
        self.transaction_list = []

    def add_transaction(self, transaction):
        set.transaction_list.append(transaction)

    def display_income_expenses(self):
        print(f"----- Month {self.month} -----")
        for transaction in self.transaction_list:
            print(transaction)


class IncomeExpenseManager:
    def __init__(self):
        self.month_list = {}

    def add_month(self, month):
        self.month_list[month] = Month(month)

    def add_transaction(self, month, transaction):
        if month in self.month_list:
            self.month_list[month].add_transaction(transaction)
            return True
        return False
    
    def display_income_expenses_by_month(self, month):
        if month in self.month_list:
            self.month_list[month].display_income_expenses()
        else:
            print("No data available for this month.")

def menu():
    manager = IncomeExpenseManager()
    while True:
        print("n1\. Add income/expense information for a month")
        print("2. Display income/expense information for a month")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            month = input ("Enter month (e.g., 01, 02, ..., 12): ")
            if month not in manager.month_list:
                manager.add_month(month)
            transaction_type = input("Enter transaction type (income/expense): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            transaction = Transaction(amount, transaction_type, description)
            if manager.add_transaction(month, transaction):
                print("Income/expense information has been added.")
            else:
                print("Error: Month does not exist.")

        elif choice == '2':
            month = input("Enter month to display income/expense information: ")
            manager.display_income_expenses_by_month(month)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try agian.")


        