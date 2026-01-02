class ScienceStudent:
    def study(self):
        return "Studying Physics and Chemistry"
class ArtsStudent:
    def study(self):
        return "Studying History and Literature"
def start_study(student):
    print(student.study())  
s1 = ScienceStudent()
s2 = ArtsStudent()
start_study(s1)
start_study(s2)
class LazyStudent:
    pass  
lazy = LazyStudent()
#start_study(lazy)
 
#Abstract Base Class (ABCs) Version  
from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def study(self):
        pass
class ScienceStudent(Student):
    def study(self):
        return "Studying Physics and Chemistry"

class ArtsStudent(Student):
    def study(self):
        return "Studying History and Literature"
def start_study_abc(student: Student):
    print(student.study())
s1 = ScienceStudent()
s2 = ArtsStudent()

start_study_abc(s1)
start_study_abc(s2)

class LazyStudent(Student):
    pass
# lazy = LazyStudent() 
