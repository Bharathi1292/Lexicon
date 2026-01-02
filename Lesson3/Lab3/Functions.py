def greet(name):
    return f"Hello, {name}!"

def greet_default(name="friend"):
    return f"Hello, {name}!"

def is_even(num):
    return num % 2 == 0

def add_if_even(a, b):
    if is_even(a) and is_even(b):
        return a + b
    return 0

print(greet("Bharathi"))
print(greet_default())
print("Is number even?", is_even(4))
print("Sum of even numbers,otherwise 0: ", add_if_even(4, 10))
print("Sum of even numbers,otherwise 0: ", add_if_even(4, 7))
