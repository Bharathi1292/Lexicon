class Book:
    def __init__(self, title, name):
        self.title = title
        self.__name = name  

b = Book("Python Basics", "Good")

# print(b.__name)  

print("Accessing book name with name:", b._Book__name)

b._Book__name = "Bad"
print("Updated book name:", b._Book__name)


