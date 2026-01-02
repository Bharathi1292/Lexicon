# Global variable
counter = 0

def increase_counter():
    global counter     
    counter += 1
    print("Inside function, counter = ", counter)

print("Before function call, counter = ", counter)

increase_counter()

print("After function call, counter  = ", counter)
