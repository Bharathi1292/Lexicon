def add(x):
    return x + 2

def square(x):
    return x * x

def pipeline(value, functions):
    result = value
    for func in functions:
        result = func(result)
    return result

number = [
    add,                  
    lambda x: x * 3,         
    square                    
]
value = 4
result = pipeline(value, number)
print("Result is:", result)
