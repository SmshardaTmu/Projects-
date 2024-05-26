class Book:
    def __init__(self, book_id, title, author, publication_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}, Status: {'Available' if not book.is_borrowed else 'Borrowed'}")

    def borrow_book(self, borrower_name, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_borrowed:
                book.is_borrowed = True
                print(f"{borrower_name} borrowed '{book.title}' successfully.")
                return
        print("Book not found or already borrowed.")

    def return_book(self, borrower_name, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_borrowed:
                book.is_borrowed = False
                print(f"{borrower_name} returned '{book.title}' successfully.")
                return
        print("Book not found or not borrowed.")

# Sample usage:
library = Library()

# Adding books to the library
books_data = [
    (1, "AI&ML", "John Smith", 2020),
    (2, "Data Science", "Alice Johnson", 2019),
    (3, "Python", "Michael Brown", 2021),
    (4, "PowerBi", "Emily Wilson", 2018),
    (5, "SQL", "David Lee", 2020)
]

for book_data in books_data:
    book = Book(*book_data)
    library.add_book(book)

# Display available books
library.display_books()

# Borrowing and returning books
borrower_name = input("Enter your name: ")
while True:
    action = input("Do you want to borrow (B) or return (R) a book? (Enter 'Q' to quit): ").upper()
    if action == 'Q':
        break
    elif action == 'B':
        book_id = int(input("Enter the ID of the book you want to borrow: "))
        library.borrow_book(borrower_name, book_id)
    elif action == 'R':
        book_id = int(input("Enter the ID of the book you want to return: "))
        library.return_book(borrower_name, book_id)
    else:
        print("Invalid action. Please enter 'B', 'R', or 'Q'.")

# Display updated book status
library.display_books()
