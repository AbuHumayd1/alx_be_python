class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private by convention

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out if available."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Mark a book as returned."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        """List all books that are not checked out."""
        print("Available Books:")
        available = False
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
                available = True
        if not available:
            print("No books available.")

