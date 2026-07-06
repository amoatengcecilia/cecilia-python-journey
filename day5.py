# DAY 5: Lists

# 1. Creating a list
students = ["Ama", "Kojo", "Cecilia"]
print(students)

print()

# 2. Accessing list items
print("First student:", students[0])
print("Last student:", students[-1])

print()

# 3. Modifying a list
students[1] = "Yaw"
print("After modifying:", students)

print()

# 4. Adding items with append()
students.append("Grace")
print("After append:", students)

print()

# 5. Adding items with insert()
students.insert(2, "Collins")
print("After insert:", students)

print()

# 6. Another example
numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers[3] = 35

print("Numbers:", numbers)