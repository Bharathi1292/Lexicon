class Student:
    def __init__(self, name, math, english, science):
        self.name = name
        self.scores = {"Math": math, "English": english, "Science": science}

    def __str__(self):
        return "\n".join([f"{subject}: {score}" for subject, score in self.scores.items()])

student = Student("Bharathi", 90, 85, 92)
print(student)
