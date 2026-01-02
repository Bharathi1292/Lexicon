import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function...")
        result = func(*args, **kwargs)
        print("After calling the function...")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

print("Function name:", greet.__name__)
print("Function docstring:", greet.__doc__)

greet("Bharathi Dibbidi")
