class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def go_to_school(cls):
        print('i am going to school')

anna = Student('Anna','MIT')
anna.go_to_school()