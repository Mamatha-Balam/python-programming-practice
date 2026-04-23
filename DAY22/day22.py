# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))

# Intersection
print(set1.intersection(set2))

# Difference
print(set1.difference(set2))

# Symmetric Difference
print(set1.symmetric_difference(set2))


# Membership testing
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)       # True
print(6 not in my_set)   # True


# Practical example
students_A = {"A", "B", "C"}
students_B = {"B", "C", "D"}

print("Common students:", students_A.intersection(students_B))
print("All students:", students_A.union(students_B))
print("Only in A:", students_A.difference(students_B))