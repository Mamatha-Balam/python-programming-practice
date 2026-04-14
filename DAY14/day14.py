# Example 1: Rectangular pattern (3x3)
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # New line after each row


# Example 2: Triangle pattern
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# Example 3: Number pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Example 4: Reverse triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()