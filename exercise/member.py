#  Member Class (Base) 
class Member:
    BORROW_LIMIT = 3  

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  

    def borrow_book(self, book):
        if not book.available: ################
            print(f"Cannot borrow: '{book.title}' is not available.")
            return False
        if len(self.borrowed_books) >= self.BORROW_LIMIT:
            print(f"Limit reached! {self.name} cannot borrow more than {self.BORROW_LIMIT} books.")
            return False

        book.borrow()######
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed: '{book.title}'")
        return True

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"{self.name} did not borrow '{book.title}'.")
            return False

        book.return_book()######
        self.borrowed_books.remove(book)
        print(f"{self.name} returned: '{book.title}'")
        return True

    def __str__(self):
        return f"Member ID: {self.member_id} | Name: {self.name} | Borrowed: {len(self.borrowed_books)}"
