num = [2, -12, 15, 3, 1, -5]

squares = []
for item in num:
    squares.append(item ** 2)

print("Squares using loop:", squares)

squares1 = [item ** 2 for item in num]
print("Squares using comprehension:", squares1)

positive_numbers = [item for item in num if item > 0]
print("Positive numbers:", positive_numbers)
