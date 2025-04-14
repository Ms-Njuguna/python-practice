class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

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
