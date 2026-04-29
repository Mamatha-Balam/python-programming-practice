# Right Triangle Pattern
def right_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

right_triangle(5)


# Pyramid Pattern
def pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

pyramid(5)


# Hollow Square Pattern
def hollow_square(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * rows)
        else:
            print("*" + " " * (rows - 2) + "*")

hollow_square(5)


# Additional Practice: Reverse Triangle
def reverse_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

reverse_triangle(5)