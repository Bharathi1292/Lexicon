base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

for i in range(exponent):
    result *= base

print("Power of the two integers:", result)

