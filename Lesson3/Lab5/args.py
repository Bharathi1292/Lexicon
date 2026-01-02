def sum_of_values(*args):
    return sum(args)

def max_of_value(*args):
    if not args:   
        return None
    return max(args)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def mixed(a, *args, **kwargs):
    print(f"Required argument a: {a}")
    
    if args:
        print("arguments (*args):")
        for item in args:
            print(" -", item)
    else:
        print("No arguments.")
    
    if kwargs:
        print("Keyword arguments (**kwargs):")
        for key, value in kwargs.items():
            print(f" - {key}: {value}")
    else:
        print("No keyword arguments.")

print(sum_of_values(1, 2, 3, 4))
print(max_of_value(10, 50, 3, 2))
print_kwargs(name="Bharathi", age=33, hobby="Dancing")
mixed(5, 10, 15, x=1, y=2)
