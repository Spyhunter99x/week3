class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display_book(self):
        status = "Issued" if self.is_issued else "Available"

        print(
            f"{self.book_id:<10}"
            f"{self.title:<30}"
            f"{self.author:<25}"
            f"{status:<15}"
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added successfully.')

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print("Cannot remove an issued book.")
                    return

                self.books.remove(book)
                print(f'Book "{book.title}" removed successfully.')
                return

        print("Book not found.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        print("\n---------------- Library Books ----------------")
        print(
            f"{'ID':<10}"
            f"{'Title':<30}"
            f"{'Author':<25}"
            f"{'Status':<15}"
        )
        print("-" * 80)

        for book in self.books:
            book.display_book()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print("Book is already issued.")
                else:
                    book.is_issued = True
                    print(f'Book "{book.title}" issued successfully.')
                return

        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    print("Book was not issued.")
                else:
                    book.is_issued = False
                    print(f'Book "{book.title}" returned successfully.')
                return

        print("Book not found.")


# Creating Library object
library = Library()

# Adding books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Object Oriented Programming", "James Brown"))
library.add_book(Book(103, "Data Structures", "Robert Martin"))

# Display books
library.display_books()

# Issue a book
library.issue_book(101)

# Display books again
library.display_books()

# Return book
library.return_book(101)

# Remove book
library.remove_book(103)

# Display final list
library.display_books()