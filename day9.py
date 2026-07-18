# ================================
# Day 9 - Introduction to OOP
# Student Management System
# ================================


class Student:
    # Constructor
    def __init__(self, name, age, course, score):
        self.name = name
        self.age = age
        self.course = course
        self.score = score

    # Display student information
    def display_student(self):
        print("\n------ Student Information ------")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print(f"Score  : {self.score}")

    # Determine grade
    def check_grade(self):
        if self.score >= 80:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        elif self.score >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"Grade  : {grade}")

        # Check pass or fail

    def is_pass(self):
        if self.score >= 50:
            print("Status : PASS")
        else:
            print("Status : FAIL")

        # Update student's score

    def update_score(self, new_score):
        self.score = new_score
        print(f"\nScore updated successfully!")
        print(f"New Score: {self.score}")


# -------------------------------
# Main Program
# -------------------------------

print("===================================")
print(" Student Management System ")
print("===================================")

students = []

number = int(input("How many students do you want to enter? "))

for i in range(number):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    score = float(input("Score: "))

    student = Student(name, age, course, score)
    students.append(student)

print("\n===================================")
print(" STUDENT RECORDS ")
print("===================================")

for student in students:
    student.display_student()
    student.check_grade()
    student.is_pass()

    choice = input("\nDo you want to update this student's score? (yes/no): ").lower()

    if choice == "yes":
        new_score = float(input("Enter the new score: "))
        student.update_score(new_score)

        print("\nUpdated Student Record")
        student.display_student()
        student.check_grade()
        student.is_pass()

    print("-----------------------------------")