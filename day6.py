# Student Grade Manager

students = []
scores = []

number_of_students = int(input("How many students do you want to enter? "))

# Collect student information
for i in range(number_of_students):
    name = input("Enter student name: ")
    score = int(input("Enter score: "))

    students.append(name)
    scores.append(score)


# Display student grade
print("\nStudent Results")

for i in range(len(students)):
    score = scores[i]

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{students[i]} scored {score} - Grade {grade}")