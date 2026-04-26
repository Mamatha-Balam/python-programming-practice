# Positional Arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)


# Keyword Arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=25, name="Bob")


# Default Values
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice")
greet("Bob", 25)


# Additional Example
def add(a, b=10):
    return a + b

print(add(5))       # Uses default value
print(add(5, 3))    # Overrides default value