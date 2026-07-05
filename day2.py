name = input("What is your name?")
age = int(input("How old are you?"))
career = input("What's your dream career?")

print()
print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"Your dream is to become a {career}.")
print("Keep learning!")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")