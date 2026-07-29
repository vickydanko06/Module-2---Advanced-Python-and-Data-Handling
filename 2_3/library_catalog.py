"""
Exercise: Library Catalog
Module 2 — Advanced Python & Data Handling
Estimated time: 45 minutes

Objective: Build three classes — Book, EBook (inherits from Book), and Catalog —
using OOP principles: encapsulation, inheritance, and method overriding.
"""


# ============================================================
# Book — base class
# ============================================================

class Book:
    """Represents a physical book in the library.

    Physical books can only be checked out by one person at a time,
    so checked_out is a boolean (True/False).

    This comment was from starter file. Left as is.
    """

    def __init__(self, title, author, year):
        """
        This represents a book with a title, author, and a year where the year needs to be a positive integer. if not, it will raise an error on the year. 

        """
        if year <= 0:
            raise ValueError("Year must be a positive integer")
        
        self.title = title
        self.author = author
        self.year = int(year)
        self.checked_out = False

        if year <= 0:
            raise ValueError (f"year must be a positive integer")
        self.year = year
        pass

    def check_out(self):
        """This function checks to see if the book was already checked out if so it raises a valueerror to say it is already checked out if not it will check the book out.

        """
        if self.checked_out == True:
            raise ValueError(f"The book is already checked out")
        self.checked_out = True
        pass

    def return_book(self):
        """This function checks to see if the book is on the shelf if so it raises a valueerror to say that the book was not currently checked out. if not, it will check the book back into the catalog.

        """
        if self.checked_out == False:
            raise ValueError(f"The book not currently checked out")
        self.checked_out = False
        pass

    def __repr__(self):
        """
        This function allows for humans to be able to read the out put easier. 
        """
        status = "✓" if self.checked_out else "✗"
        return f"[Book: {self.title}, {self.author}, {self.year} - checked out: {status}]"
        
        pass


# ============================================================
# EBook — subclass of Book
# ============================================================

class EBook(Book):
    """An electronic book. Inherits from Book.

    Why inherit from Book? EBook shares most behaviour (title, author, year,
    catalog methods). Inheritance lets us reuse that and only override what
    genuinely differs.

    Key difference: digital files can be checked out by MULTIPLE users at once,
    so we replace the boolean with an integer counter (_checkout_count).

    This comment was from the starter file. Did not edit
    """

    def __init__(self, title, author, year, file_size_mb):
        """
        This represents an Ebook with a title, author, year and file size.
        """
        super().__init__(title, author, year)
        self.file_size_mb = float(file_size_mb)
        self.checkout_count = 0
  
        pass

    @property
    def checked_out(self):
        """Returns True if at least one user checked out an EBook."""
        return self.checkout_count >= 1

        pass

    @checked_out.setter
    def checked_out(self, value):
        # Book.__init__ tries to set checked_out = False.
        # We intercept that here and do nothing — EBook uses _checkout_count instead.
        pass

    def check_out(self):
        """
        This function will increase the count for the check out when the book is checked out.
        """
        
        self.checkout_count += 1
        pass

    def return_book(self):
        """
        This function checks to see if the book has copies out. if there are no copies out it returns an error message. if there are copies out one is returned and the counter decreases by one.
        """
        if self.checkout_count == 0:
            raise ValueError (f"This book currently has 0 checked out copies.")
        self.checkout_count -= 1

    def __repr__(self):
        """Return a string like:
        EBook('Title', 'Author', year, 15.2 MB) [2 active checkout(s)]
        """
        # TODO: implement __repr__ — include file_size_mb and _checkout_count

        status = self.checkout_count
        return f"[Book: {self.title}, {self.author}, {self.year}, {self.file_size_mb} - {status} active checkout(s)]"
        pass


# ============================================================
# Catalog — container and search layer
# ============================================================

class Catalog:
    """Holds a collection of Book and EBook objects.

    Design decision: we store books in a plain list (self.books).
    For a production library you'd use a database, but a list is fine
    for this exercise.
    """

    def __init__(self):
        self.books = []   # store your Book and EBook objects here

    def add_book(self, book):
        """Add a Book or EBook to the catalog."""
        self.books.append(book)

    def search_by_author(self, author):
        """Return all books where the author is being searched

        """
        return [
        book
        for book in self.books
        if author.lower() in book.author.lower()
    ]
        pass

    def search_by_title(self, keyword):
        """Return all books whose title matches even if its a partial match

        """
        return [book for book in self.books if keyword.lower() in book.title.lower()]
        pass

    def get_available(self):
        """
        Returns the available books that are not checked out
        """
        return[
        book
        for book in self.books
        if not book.checked_out
    ]
        
        pass
    def summary(self):
        """Print a summary: total books, available, checked out, ebooks.

        TODO: compute counts and print them
        """
        total_books = len(self.books)

        available = sum(1 for book in self.books if not book.checked_out)

        checked_out = sum(1 for book in self.books if book.checked_out)

        ebooks = sum(1 for book in self.books if isinstance(book, EBook))
        print(f"Total books: {total_books}")
        print(f"Available: {available}")
        print(f"Checked out: {checked_out}")
        print(f"EBooks: {ebooks}")
        pass


# ============================================================
# Tests — run these after implementing all three classes
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Library Catalog — Tests")
    print("=" * 60)

    catalog = Catalog()
    catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
    catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
    catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))


    results = catalog.search_by_title("python")
    print(f"\nsearch_by_title('python'): {results}")   # should find Python Crash Course

    catalog.books[0].check_out()
    available = catalog.get_available()
    print(f"Available: {len(available) if available is not None else '?'} books")   # should be 2

    catalog.summary()

    # EBook multi-checkout demo
    print("\nEBook multi-checkout demo:")
    ebook = catalog.books[2]
    ebook.check_out()
    ebook.check_out()
    try:
        print(f"  After 2 checkouts: {ebook}")
    except TypeError:
        print("  After 2 checkouts: (implement __repr__ to see output)")
    ebook.return_book()
    try:
        print(f"  After 1 return   : {ebook}")
    except TypeError:
        print("  After 1 return   : (implement __repr__ to see output)")