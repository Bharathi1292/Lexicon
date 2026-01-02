class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade 

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade

    def __str__(self):
        return f"{self.name}: {self.grade}"

s1 = Student("Bharathi", 85)
s2 = Student("Varma", 92)
s3 = Student("Mokshu", 78)
print(s1 < s2)  
print(s2 < s3)  
students = [s1, s2, s3]
students.sort()
for s in students:
    print(s)
