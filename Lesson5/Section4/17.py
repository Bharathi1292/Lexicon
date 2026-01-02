counter = 0
def outer():
    counter = 10
    def increment_local():
        counter = 100
        print("Inside increment_local:", counter) 
    def increment_nonlocal():
        nonlocal counter 
        counter += 5
        print("Inside increment_nonlocal:", counter)
    def increment_global():
        global counter  
        counter += 1
        print("Inside increment_global:", counter)
    print("Before any increments:", counter)  
    increment_local()
    print("After increment_local:", counter)  
    increment_nonlocal()
    print("After increment_nonlocal:", counter)  
    increment_global()
    print("After increment_global:", counter)  
print("Global counter before:", counter)
outer()
print("Global counter after:", counter)
