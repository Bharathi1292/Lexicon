class StudentGrades:
    def __init__(self, **grades):
        self.grades = grades

    def __str__(self):
        return "\n".join([f"{subject.capitalize()}: {score}" for subject, score in self.grades.items()])

student = StudentGrades(math=95, english=88, science=92)
print(student)
