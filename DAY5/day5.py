# String to Integer
num_string = "123"
print(type(num_string))

num_int = int(num_string)
print(num_int)
print(type(num_int))


# Float to Integer
num_float = 3.14
num_int = int(num_float)

print(num_int)        # Output: 3
print(type(num_int))  # int


# Integer to String
num_int = 123
print(type(num_int))

num_string = str(num_int)
print(num_string)
print(type(num_string))


# Float to String
num_float = 3.14
print(type(num_float))

num_string = str(num_float)
print(num_string)
print(type(num_string))


# Practical Example (User Input)
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Convert to integers before addition
result = int(num1) + int(num2)

print("Sum is:", result)