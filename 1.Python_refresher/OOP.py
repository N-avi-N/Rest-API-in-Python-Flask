
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)


student = Student('Anne', (90, 90, 93, 78, 90))
print(student.name)
print(student.grades)
print(student.average())


student2 = Student('Rolf', (90, 90, 90, 90, 90))
print(student2.name)
print(student2.grades)
print(student2.average())