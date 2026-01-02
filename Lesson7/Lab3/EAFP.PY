def divide(a, b):
    try:
        result = a / b           
    except ZeroDivisionError:   
        print("Error: Division by zero is not possible!")
        return None
    except Exception as e:      
        print("Error:", e)
        return None
    else:
        return result            
    
print("Result of 10/2 is : ", divide(10, 2))  

print("Result of '10'/2 is : ", divide("10", 2))  

print("Result of 10/0 is :", divide(10, 0))    
