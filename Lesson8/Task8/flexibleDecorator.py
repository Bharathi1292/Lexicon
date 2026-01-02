import functools
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Run {i + 1} of {times}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(2)
def greet(name):
    print(f"Hello, {name}!")

@repeat(3)
def add(a, b):
    print(f"{a} + {b} = {a + b}")
greet("Bharathi")
print("---")
add(3, 5)
