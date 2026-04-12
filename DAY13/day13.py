# Length of string
string = "Hello, World!"
print(len(string))


# Lowercase and Uppercase
print(string.lower())
print(string.upper())


# Strip (remove spaces)
text = "  Hello Python  "
print(text.strip())


# Replace
text = "Hello, World!"
print(text.replace("Hello", "Hi"))


# Split
fruits = "apple,orange,banana"
print(fruits.split(","))


# Startswith and Endswith
text = "Hello, World!"
print(text.startswith("Hello"))
print(text.endswith("World!"))


# Count and Find
text = "Hello, World!"
print(text.count("l"))
print(text.find("o"))


# isdigit and isalpha
num = "12345"
print(num.isdigit())

word = "Python"
print(word.isalpha())