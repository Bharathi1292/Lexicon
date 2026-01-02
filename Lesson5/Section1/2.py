class Employee:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation

    def __str__(self):
        return (
            f"Employee Details:\n"
            f"  Name : {self.name}\n"
            f"  Age  : {self.age}\n"
            f"  Grade: {self.designation}"
        )
Employee1 = Employee("Bharathi", 33, "Developer")
print(Employee1)
