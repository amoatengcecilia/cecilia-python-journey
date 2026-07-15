contacts_list = {}
n = int(input("How many contacts do you want to enter: "))
for i in range(n):
    name = input("Name: ")
    number = input("Phone number: ")

    contacts_list[name] = number


file = open("contact.txt", "a")

for name, number in contacts_list.items():
    file.write(f"{name}: {number}\n")
file.close()

file = open("contact.txt", "r")

print("\nSaved Contacts")
print("-" * 20)

print(file.read())

file.close()