# Creating tuples
fruits = ("apple", "banana", "orange")
coordinates = (3.14, 2.71)

print(fruits)
print(coordinates)


# Accessing elements
print(fruits[0])  # apple
print(fruits[2])  # orange


# Tuple packing and unpacking
person = ("John", 30, "New York")

name, age, city = person

print(name)
print(age)
print(city)


# Tuple functions
numbers = (5, 2, 8, 1, 7)

print(len(numbers))
print(max(numbers))
print(min(numbers))


# Tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)   # Concatenation
print(tuple1 * 3)        # Repetition


# Additional example
data = ("Python", 2026, True)

for item in data:
    print(item)