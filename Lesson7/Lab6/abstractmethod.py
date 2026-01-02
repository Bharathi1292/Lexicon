from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def study(self):
        pass  

class LazyStudent(Student):
    pass

#lazy = LazyStudent() 

class ScienceStudent(Student):
    def study(self):
        return "Studying Physics and Chemistry"

class ArtsStudent(Student):
    def study(self):
        return "Studying History and Literature"

def start_study(student: Student):
    print(student.study())

s1 = ScienceStudent()
s2 = ArtsStudent()

start_study(s1)  
start_study(s2)  
