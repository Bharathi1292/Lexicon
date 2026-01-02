numbers = (10, 2, 3, 4, 5, 6, 8, 9,7,26,18)

even_numbers = ()

for i in numbers:
    if i % 2 == 0:
        even_numbers += (i,)  

print("Even numbers in the tuple:", even_numbers)
