#exercise 1
class StudentManagement():
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def is_adult(self):
        if self.age >= 18:
            print("You are adult")
        else:
            print("You are a young boy")

    def introduction(self):
        print(f"my name  is : {self.name}, I am : {self.age} years old and I am in {self.department} ")


#  Book Class 