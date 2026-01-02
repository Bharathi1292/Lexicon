class People:
    def __init__(self):
        print("Constructor of People")

class Student(People):
    def __init__(self):
        super().__init__()
        print("Constructor of Student")

class Employee(People):
    def __init__(self):
        super().__init__()
        print("Constructor of Employee")

class WorkingStudent(Student, Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of WorkingStudent")
obj = WorkingStudent()
print("Actual MRO =", WorkingStudent.mro())
