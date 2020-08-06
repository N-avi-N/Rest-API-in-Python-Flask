
class ClassTest:
    def instance_method(self):
        print(f'Calling instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Calling class_method of {cls}')

    @staticmethod
    def static_method():
        print(f'Calling static_method')

test = ClassTest()

ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'Book({self.name}, {self.book_type}, {self.weight})'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight)

# book = Book('Harry Potter', 'hardcover', 1500)
book = Book.hardcover('Harry Potter', 1500)
light = Book.paperback('Python 101', 600)
print(book, '\n', light)