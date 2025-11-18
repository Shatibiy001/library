from member import Member
#  Bonus C: Subclasses
class StudentMember(Member):
    def __init__(self, name, member_id, school):
        super().__init__(name, member_id)
        self.school = school

    def __str__(self):
        return f"Student: {self.name} ({self.school}) | Borrowed: {len(self.borrowed_books)}"


