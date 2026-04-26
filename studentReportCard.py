class Subject:

    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks  

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"


class Student:

    def __init__(self, name, roll_no):
        self.name     = name
        self.roll_no  = roll_no
        self.subjects = []     

    def add_subject(self, name, marks):
        subject = Subject(name, marks)
        self.subjects.append(subject)


class ReportCard:

    def __init__(self, student):
        self.student = student

    def total_marks(self):
        return sum(s.marks for s in self.student.subjects)

    def percentage(self):
        total = self.total_marks()
        out_of = len(self.student.subjects) * 100
        return round((total / out_of) * 100, 2)

    def final_grade(self):
        pct = self.percentage()
        if pct >= 90:
            return "A+"
        elif pct >= 80:
            return "A"
        elif pct >= 70:
            return "B"
        elif pct >= 60:
            return "C"
        elif pct >= 50:
            return "D"
        else:
            return "F"

    def result(self):
        return "PASS " if self.percentage() >= 50 else "FAIL ❌"

    def display(self):
        s = self.student
        print("\n============================")
        print("       📋 REPORT CARD")
        print("============================")
        print(f"  Name     : {s.name}")
        print(f"  Roll No  : {s.roll_no}")
        print("----------------------------")

        for sub in s.subjects:
            print(f"  {sub.name:<12} : {sub.marks}   — {sub.grade()}")

        total  = self.total_marks()
        out_of = len(s.subjects) * 100

        print("----------------------------")
        print(f"  Total      : {total} / {out_of}")
        print(f"  Percentage : {self.percentage()}%")
        print(f"  Grade      : {self.final_grade()}")
        print(f"  Result     : {self.result()}")
        print("============================")


print("\n============================")
print("   📋 Student Report Card")
print("============================")

name    = input("Student name: ")
roll_no = input("Roll number: ")

student = Student(name, roll_no)

num = int(input("How many subjects: "))

for i in range(num):
    sub_name = input(f"\nSubject {i+1} name: ")
    marks    = int(input(f"Marks (out of 100): "))
    student.add_subject(sub_name, marks)

card = ReportCard(student)
card.display()