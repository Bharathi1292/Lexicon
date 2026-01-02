import time

def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper

@execution_time
def process_numbers():
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for n in numbers:
        total += n
    print("Sum of numbers :", total)

process_numbers()
