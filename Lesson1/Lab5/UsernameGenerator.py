firstName = input("Enter your firstname : ")
lastName  = input("Enter your lasstname : ")
birthYear = input("Enter your birth year: ")

first_part = firstName[:2]         
second_part = lastName[-3:]         
third_part = birthYear[-2:]  

username = first_part + second_part + third_part

print("Generated username is : ", username)
