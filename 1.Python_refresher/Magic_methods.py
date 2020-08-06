
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} age is {self.age}'

    def __repr__(self):
        return f'Person({self.name}, {self.age})'

bob = Person('Bob', 35)
print(bob)


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({'name': name, 'price': price})

    def prints(self):
        for i in self.items:
            print(i)

store = Store

