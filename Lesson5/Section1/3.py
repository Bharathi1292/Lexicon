class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price!r})"

book1 = Book("What's Your Dream?", "Simon Squibb", 299)

print(book1)         
recreated = eval(repr(book1))  
print("Object recreated successfully")
