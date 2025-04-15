class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    
    # In Book class

    def borrow(self):
        if self.is_borrowed:
            print(f"{self.title} is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"{self.title} wasn't borrowed.")
        else:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")

class Library:
    def __init__(self):
        self.books = []  # starts empty

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Removed: {book}")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in library:")
            for book in self.books:
                print(f" - {book}")

    def search_by_author(self, author):
        found = [book for book in self.books if author.lower() in book.author.lower()]
        if found:
            print(f"Books by '{author}':")
            for b in found:
                print(f" - {b}")
        else:
            print(f"No books by '{author}' found.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
               book.borrow()
               return
        print("Book not found.")

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        for book in library.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.borrow()
                self.borrowed_books.append(book)
                return
        print(f"{title} is not available to borrow.")

    def return_book(self, library, title):
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                book.return_book()
                self.borrowed_books.remove(book)
                return
        print(f"{self.name} hasn't borrowed {title}.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} hasn't borrowed any books.")
        else:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f" - {book}")


# Test your classes
library = Library()

book1 = Book("Born a Crime", "Trevor Noah", 2016)
book2 = Book("The Alchemist", "Paulo Coelho", 1988)
book3 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie", 2003)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()
library.search_by_author("Chimamanda")
library.remove_book("The Alchemist")
library.list_books()

library.borrow_book("Born a Crime")
library.borrow_book("Born a Crime")  # Try borrowing it again
book1.return_book()
library.list_books()

# Create a User
user1 = User("Patricia")

# User borrows a book
user1.borrow_book(library, "Born a Crime")
user1.list_borrowed_books()
library.list_books()

# User returns the book
user1.return_book(library, "Born a Crime")
user1.list_borrowed_books()
library.list_books()