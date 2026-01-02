matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("The number in row 1, column 2 is : ",matrix [0][1])

print("The entire second row is : ",matrix [1])

diagonal = []
for i in range(len(matrix)):
    diagonal.append(matrix[i][i])
print("Diagonal elements:", diagonal)

first_column = [matrix[0][0], matrix[1][0], matrix[2][0]]
print("First column elements using indexing : ", first_column)

repeat_list = [row[0] for row in matrix]
print("Repeat using a list comprehension : ", repeat_list) 

