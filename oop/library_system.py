class Book:
    def __init__(self, title: str, author: str):
        """Initialize the book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize the EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print the details of each book in the library."""
        for book in self.books:
            print(book)
