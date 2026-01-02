def multiple(factor):

    def multiply(number):
        return number * factor
    return multiply

double = multiple(2)
triple = multiple(3)

print(double(5))  
print(triple(5))   
