# Example 1: Nested if statement
x = 10

if x > 0:
    print("x is positive.")

    if x % 2 == 0:
        print("x is even.")
    else:
        print("x is odd.")
else:
    print("x is not positive.")


# Example 2: Nested if-elif-else
score = 85

if score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

    if score >= 85:
        print("Good job!")

elif score >= 70:
    print("Grade: C")

else:
    print("Grade: Below C")


# Additional Practice
num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")