# Creating a dictionary
student = {
    "name": "Mamatha Balam",
    "age": 21,
    "course": "MCA",
    "gpa": 8.5
}

print(student)


# Accessing values
print(student["name"])
print(student["gpa"])


# Modifying values
student["age"] = 22
print(student)


# Adding new key-value pair
student["city"] = "Kurnool"
print(student)


# Removing key-value pair
student.pop("gpa")
print(student)


# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)


# Additional example
marks = {
    "math": 90,
    "science": 85,
    "english": 88
}

print("Math marks:", marks["math"])