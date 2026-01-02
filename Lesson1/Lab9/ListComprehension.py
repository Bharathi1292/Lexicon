numbers = [1,2,3,4,5,6,7,8,9] 

square_numbers= [x**2 for x in numbers]
print("Squares of the items in the list:", square_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print("The Even numbers in the List are :", even_numbers)

doubled_numbers = [x*2 for x in numbers]
print("Numbers are Doubled in the list :", doubled_numbers)

greater_numbers = [x for x in numbers if x > 5]
print("Numbers greater than 5 in the list:", greater_numbers)

strings = [f"Number: {x}" for x in numbers]
print("A list of strings Number: X for each element :", strings)