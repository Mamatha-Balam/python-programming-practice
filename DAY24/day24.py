# Default Parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Sudha")


# Calling Functions Inside Functions
def greet(name):
    return f"Hello, {name}!"

def greet_and_emphasize(name):
    greeting = greet(name)
    return greeting.upper() + "!!!"

result = greet_and_emphasize("Sudha")
print(result)


# Scope of Variables
global_variable = "I'm global"

def function_with_local_variable():
    local_variable = "I'm local"
    print(global_variable)
    print(local_variable)

function_with_local_variable()

print(global_variable)

# Uncomment to see error
# print(local_variable)