# String Concatenation
a = "Hello" + " " + "World!"
print(a)


# Possible mistake (Uncomment to see error)
# a = "Hi" + 10
# print(a)


# Correct way (type conversion)
a = "Hi " + str(10)
print(a)


# String Repetition
a = "Python " * 5
print(a)


# Pattern example
s = "Arrow"
s = ("* " * 3) + s + (" *" * 3)
print(s)


# Length of String
name = input("Enter your name: ")
length = len(name)
print("Length of your name is:", length)