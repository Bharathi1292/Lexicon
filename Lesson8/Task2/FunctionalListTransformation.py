def transform_list(numbers):
    return list(
        filter(
            lambda x: x % 2 == 0,      
            map(lambda x: x * 3, numbers)  
        )
    )

numbers = [1, 2, 3, 4, 5, 6]
result = transform_list(numbers)
print(result)
