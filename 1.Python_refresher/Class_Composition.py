
# We pass multiple objects of one class as input to another class, better than inheritance in some ways

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'Bookshelf with {len(self.books)} books'

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'

book = Book('Harry Potter')
book2 = Book('Python 101')
shelf = BookShelf(book, book2)

print(shelf)
print(shelf.books


