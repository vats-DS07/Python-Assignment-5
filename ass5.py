class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def stud_info(self):
        super().info()
        print(f"Course: {self.course}")

class exam(student):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age, course)
        self.marks = marks
    def total_marks(self):
        return sum(self.marks)
    
    def reportcard(self):
        print("STUDENT REPORT CARD")
        self.stud_info()
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total_marks()}/500")

if __name__ == "__main__":
    student = exam("VATS AGGARWAL", 18, "BCA (AI & DS)", [82, 90, 73, 92 , 88])
    student.reportcard()

       
