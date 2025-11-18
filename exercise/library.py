from student import StudentManagement
from member import Member
from st_member import StudentMember
from book import Book
from sf_member import StaffMember
#  Library Class
class Library:
    def __init__(self, name="Central Library"):
        self.name = name
        self.books = []      
        self.members = []    

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name} (ID: {member.member_id})")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # Bonus B: Search books
    def search_books(self, query="", by="title"):
        results = []
        query = query.lower()
        for book in self.books:
            if by == "title" and query in book.title.lower():
                results.append(book)
            elif by == "author" and query in book.author.lower():
                results.append(book)
        return results

    def list_all_books(self):
        print(f"\n=== {self.name} - All Books ===")
        if not self.books:
            print("No books in library.")
        for book in self.books:
            print(book)
   
    def list_all_members(self):
        print(f"\n=== Members ===")
        for member in self.members:
            print(member)
            if member.borrowed_books:
                print("   Borrowed:", ", ".join([b.title for b in member.borrowed_books]))


def main():
    #studentmanagement 
    school = StudentManagement("Dev.Afeez", "98", "Software enginering")
    school.introduction()
    # Create library
    library = Library("University Library")
 
    # Add 3 books
    b1 = Book("Things Fall Apart", "Chinua Achebe", "978-0385474542")
    b2 = Book("Python Crash Course", "Eric Mattes", "978-1593279285")
    b3 = Book("The Lion and the Jewel", "Wole Soyinka", "978-0199110837")
    b4 = Book("The Lion and the Jewel", "Wole Soyinka", "978-0199110837")

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.add_book(b4)

    # Add 2 members (with inheritance)
    m1 = StudentMember("Adeleke John", "STU001", "University of Lagos")
    m2 = StaffMember("Mrs. Chioma", "STF001", "Librarian")

    library.add_member(m1)
    library.add_member(m2)

    print("\n" + "="*50)
    print("           LIBRARY SYSTEM TEST")
    print("="*50)

    # 1. Adeleke borrows a book
    book = library.find_book("978-0385474542")
    m1.borrow_book(book)

    # 2. Mrs. adisa tries to borrow the same → fails
    m2.borrow_book(book)

    # 3. Adeleke returns the book
    m1.return_book(book)

    # 4. Mrs. adisa borrows it successfully
    m2.borrow_book(book)

    # Bonus: Search + List
    print("\n--- Searching for 'python' ---")
    results = library.search_books("python", by="title")
    for b in results:
        print(b)

    # Final status
    library.list_all_books()
    library.list_all_members()


#  Run the Program 
if __name__ == "__main__":
    main()