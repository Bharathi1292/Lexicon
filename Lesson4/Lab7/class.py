class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def student_info(self):
        
        print(f"Student Name: {self.name}, Age: {self.age}")

student1 = Student("Bharathi", 33)
student2 = Student("Varma", 40)

student1.student_info()
student2.student_info()
