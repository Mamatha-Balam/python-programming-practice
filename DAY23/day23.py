# Example 1: Simple function
def greet():
    print("Hello, World!")

greet()


# Example 2: Function with parameter
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Maya")


# Example 3: Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)


# Example 4: Multiple calls
def square(num):
    return num * num

print(square(4))
print(square(7))