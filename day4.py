# Function that greet a user
def greet(name):
    print(f"Hello {name}!")
greet("Collins")


#Function that takes name and age
def identity(name, age):
    print(f"{name} is {age} years old.")
identity("Collins", 28)



# Function that adds two numbers and prints result
def add(a, b):
    return a + b
result = add(2, 89)
print(result)


# Function that returns the square of a number
def square(a):
    return a * a
result = square(9)
print(result)


# Function that prints the multiplication table for any number
def multiples(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
multiples(4)