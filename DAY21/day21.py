# Creating sets
my_set = {1, 2, 3, 4, 5}
another_set = set([5, 6, 7, 8, 9])

print(my_set)
print(another_set)


# Adding elements
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)

print(my_set)


# Removing elements
my_set = {1, 2, 3, 4, 5}

my_set.remove(3)
print(my_set)

# Discard (no error if element not present)
my_set.discard(10)

# Pop (removes random element)
popped_element = my_set.pop()
print("Removed:", popped_element)
print("Remaining set:", my_set)


# Additional example: removing duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print("Unique values:", unique_numbers)