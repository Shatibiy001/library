#  Book Class 
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  

    def borrow(self):
        if self.available:
            self.available = False
            return f"Success: '{self.title}' has been borrowed."
        else:
            return f"Failed: '{self.title}' is already borrowed."

    def return_book(self):
        self.available = True
        return f"'{self.title}' has been returned and is now available."

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.isbn}] {self.title} by {self.author} — {status}"