import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(n):
        print(f"Calling {func.__name__}({n})")
        result = func(n)
        print(f"{func.__name__}({n}) returned {result}")
        return result
    return wrapper

@log_calls
def factorial(n):
  
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial result:", factorial(5))
