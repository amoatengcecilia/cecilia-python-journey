# A few practice examples showing
student_scores = {
    "Ama": 85,
    "Kojo": 72
}
student_scores["Cecilia"] = 95
student_scores["Kojo"] = 80

print(student_scores["Ama"])
print(student_scores.get("Yaw"))

for student in student_scores:
    print(student, student_scores[student])
print()

# PHONE BOOK MINI PROJECT

phone_book = {}

n = int(input("How many contacts? "))

for i in range(n):
    name = input("Name: ")
    number = input("Phone number: ")
    phone_book[name] = number

print("\nPhone Book")
print("-" * 20)
for name, number in phone_book.items():
    print(f"{name}: {number}")
