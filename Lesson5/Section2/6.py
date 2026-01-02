class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title == other.title and
                self.author == other.author and
                self.year == other.year)

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

book1 = Book("What's Your Dream?", "Simon Squibb", 2025)
book2 = Book("What's Your Dream?", "Simon Squibb", 2025)
book3 = Book("Brave New World", "Aldous Huxley", 1932)

print(book1 == book2)  
print(book1 == book3) 
print(book1)          