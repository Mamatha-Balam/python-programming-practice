# Example 1: if statement
age = 18

if age >= 18:
    print("You are an adult.")


# Example 2: if-else statement
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Example 3: if-elif-else statement
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Practical Example
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")