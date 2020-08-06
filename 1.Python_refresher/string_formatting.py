from datetime import date

name = 'Bob'
name2 = 'World'

print(f'Hello, {name} !')
print(f'Hello, {name2} !')

print('Hello, {} !'.format(name2))

print('Hello {} ! today is {}'.format(name2, date.today()))