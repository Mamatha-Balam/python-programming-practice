# Example 1: Print numbers from 1 to 5
num = 1

while num <= 5:
    print(num)
    num += 1


# Example 2: Sum of numbers from 1 to 10
num = 1
sum_of_numbers = 0

while num <= 10:
    sum_of_numbers += num
    num += 1

print("Sum of numbers from 1 to 10:", sum_of_numbers)


# Example 3: Infinite loop example (Don't run)
# while True:
#     print("This will run forever")


# Example 4: User input loop
count = 1

while count <= 3:
    name = input("Enter your name: ")
    print("Hello", name)
    count += 1