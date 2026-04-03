# Example 1: Order of execution (Error example)
# Uncomment to see error
# print(a)
# a = "Hello"

# Correct version
a = "Hello"
print(a)


# Example 2: Indentation error (Wrong)
# Uncomment to see error
# a = 10
# b = 5
#  print(a / b)

# Correct version
a = 10
b = 5
print(a / b)


# Example 3: BODMAS rule
result = 10 + 5 * (2 ** 3) - 6 / 2
print(result)


# Step-by-step understanding
# 2 ** 3 = 8
# 5 * 8 = 40
# 6 / 2 = 3
# 10 + 40 - 3 = 47


# More examples
print(10 / 2 + 3)      # Output: 8.0
print(10 / (2 + 3))    # Output: 2.0