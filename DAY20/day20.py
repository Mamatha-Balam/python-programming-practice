# Creating dictionary
student = {
    "name": "Mamatha Balam",
    "age": 21,
    "course": "MCA",
    "gpa": 8.5
}

# Modifying value
student["gpa"] = 9.0

# Adding new key-value pair
student["university"] = "XYZ University"

print(student)


# Dictionary methods
keys = student.keys()
values = student.values()

print("Keys:", keys)
print("Values:", values)


# Check if key exists
if "course" in student:
    print("Course:", student["course"])


# Remove key-value pair
removed_value = student.pop("age")
print("Removed Value:", removed_value)

print(student)


# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)