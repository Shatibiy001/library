from member import Member
class StaffMember(Member):
    def __init__(self, name, member_id, position):
        super().__init__(name, member_id)
        self.position = position

    def __str__(self):
        return f"Staff: {self.name} ({self.position}) | Borrowed: {len(self.borrowed_books)}"
