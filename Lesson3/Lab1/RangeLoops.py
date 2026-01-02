print("Odd numbers from 1 to 20:")
for num in range(1, 21):
    if num % 2 != 0:
        print(num)

total_sum = 0
for num in range(1, 101):
    total_sum += num
print("Sum of numbers from 1 to 100:", total_sum)

user_num = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication table for {user_num}:")
for i in range(1, 11):
    print(f"{user_num} x {i} = {user_num * i}")
