def outer_function():
    count = 0  

    def inner_function():
        nonlocal count  
        count += 1
        print("Inside inner_function, count = ", count)

    print("Before calling inner_function, count = ", count)
    inner_function()
    print("After calling inner_function, count = ", count)

outer_function()
