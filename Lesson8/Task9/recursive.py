import time
from functools import lru_cache

def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)
@lru_cache(maxsize=None)
def memo(n):
    if n <= 1:
        return n
    return memo(n-1) + memo(n-2)
n = 15
start = time.time()
print("Naive recursive result:", recursive(n))
end = time.time()
print("Time taken (naive):", end - start, "seconds")
print("---")
start = time.time()
print("Memoized recursive result:", memo(n))
end = time.time()
print("Time taken (memoized):", end - start, "seconds")
