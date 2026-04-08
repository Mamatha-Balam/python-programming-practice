# AND Operator
a = True
b = False

print(a and b)  # False

x = 10
y = 5

print((x > 0) and (y < 10))   # True
print((x > 0) and (y > 10))   # False


# OR Operator
a = True
b = False

print(a or b)  # True

print((x > 0) or (y < 10))   # True
print((x < 0) or (y > 10))   # False


# NOT Operator
a = True
print(not a)  # False

print(not (x > y))  # False
print(not (x < y))  # True


# Complex Logical Expression
x = 5
y = 10
z = 15

result = (x < y) and (y < z) or (x == z)
print(result)  # True


# Additional Practice
num = 8

print((num > 5) and (num < 10))  # True
print((num < 5) or (num == 8))   # True
print(not (num == 8))            # False