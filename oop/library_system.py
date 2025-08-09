# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize the title and author of the book."""
        self.title = title
        self.author = author


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size in MB."""
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author} - {self.file_size}MB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and number of pages."""
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author} - {self.page_count} pages"


# Composition - Library
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print the details of all books in the library."""
        for book in self.books:
            print(book)
