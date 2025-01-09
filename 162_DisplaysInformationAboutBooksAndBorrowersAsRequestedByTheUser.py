# Write a program that manages a library system using object-oriented programming.
# Algorithm: 1_Create a Book class with attributes like title, author, and status(borrowed/ available). 2_Create a Borrower class with attributes like name and a list of borrowed books. 3_Create a LibraryManager class to manage the lists of books and borrowers.
#4_Main method include: Add a new book to the library. Add a new borrower. Borrow a book. Return a book. Display the list of books. Display the list of borrowers.. 5_Provide a user interface to input commands manage the library.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title}, Author: {self.author}, Status: {status}"
    

class Borrower:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.is_borrowed = True
            return True
        return False
    
    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title == title:
                self.borrowed_books.remove(book)
                book.is_borrowed = False
                return True
            return False
        
    def __str__(self):
        book_list = ", ".join(book.title for book in self.borrowed_books)
        return f"Borrower: {self.name}, Borrowed books: {book_list}"
    

class LibraryManager:
    def __init__(self):
        self.book = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def borrow_book(self, borrower_name, book_title):
        borrower = self.find_borrower(borrower_name)
        book = self.find_book(book_title)
        if borrower and book:
            return borrower.borrow_book(book)
        return False
    
    def return_book(self, borrower_name, book_title):
        borrower = self.find_borrower(borrower_name)
        if borrower:
            return borrower.return_book(book_title)
        return False
    
    def display_books(self):
        for book in self.books:
            print(book)

    def display_borrowers(self):
        for borrower in self.borrowers:
            print(borrower)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def find_borrower(self, name):
        for borrower in self.borrowers:
            if borrower.name == name:
                return borrower
        return None
    
def menu():
    library = LibraryManager()
    while True:
        print("\n1. Add Book")
        print("2. Add Borrower")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Book List")
        print("6. Display Borrower List")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book added.")

        elif choice == '2':
            name = input("Enter borrower's name: ")
            borrower = Borrower(name)
            library.add_borrower(borrower)
            print("Borrower added.")

        elif choice == '3':
            name = input("Enter borrower's name: ")
            title = input("Enter title of the book to borrow: ")
            if library.borrow_book(name, title):
                print("Book borrowed.")
            else:
                print("Cannot borrow the book.")

        elif choice == '4':
            name = input("Enter borrower's name: ")
            title = input("Enter title of the book to return: ")
            if library.return_book(name, title):
                print("Book returned.")
            else:
                print("Cannot return the book")

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            library.display_borrowers()

        elif choice == '7':
            print("Exiting the program.")
            break

        else: 
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    menu()

            


