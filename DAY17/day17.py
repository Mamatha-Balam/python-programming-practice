# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed_list = [1, "apple", True, 3.14]

print(numbers)
print(fruits)
print(mixed_list)


# Accessing elements
print(fruits[0])  # apple
print(fruits[2])  # orange


# Modifying elements
fruits[1] = "grape"
print(fruits)


# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)   # Concatenation
print(list1 * 3)       # Repetition


# List methods
fruits = ["apple", "banana", "orange"]

# Add element
fruits.append("grape")
print(fruits)

# Remove element
fruits.remove("banana")
print(fruits)

# Sort list
fruits.sort()
print(fruits)


# Additional practice
numbers = [5, 2, 9, 1]

numbers.sort()
print("Sorted:", numbers)