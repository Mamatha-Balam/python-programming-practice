# Example 1: break statement
for num in range(1, 6):
    if num == 3:
        break
    print(num)


# Example 2: continue statement
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)


# Example 3: pass statement
for num in range(1, 6):
    pass


# Example 4: Practical example
for num in range(1, 11):
    if num == 5:
        print("Skipping 5")
        continue
    if num == 8:
        print("Stopping at 8")
        break
    print(num)