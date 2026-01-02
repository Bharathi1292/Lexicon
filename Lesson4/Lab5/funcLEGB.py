# Global variable
name = "Varma Dibbidi"

def outer_function():
    name = "Mokshu Dibbidi"

    def inner_function():
        name = "Bharathi Dibbidi"
        print("Inside inner function:", name) 

    print("Inside outer function before calling inner:", name)  
    inner_function()
    print("Inside outer function after calling inner:", name)   

print("Outside all functions (global):", name)  
outer_function()
print("Outside all functions again (global):", name)
