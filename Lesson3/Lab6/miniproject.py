user_input = input("Enter numbers separated by spaces: ")

numbers = [int(num) for num in user_input.split()]


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))
