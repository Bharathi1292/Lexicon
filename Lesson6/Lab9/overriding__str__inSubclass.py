class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  

    def __str__(self):
        base_str = super().__str__()  
        return f"{base_str} | File size: {self.file_size} MB"

book = Book("Python Basics", "Bharathi")
ebook = EBook("Python Advanced", "Varma", 5)

print(book)  
print(ebook)  
