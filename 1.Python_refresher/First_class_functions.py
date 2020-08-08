
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be zero')

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)

print(result)

############################################################################################################################

def search(sequence, expected, finder):
    for elm in sequence:
        if finder(elm) == expected:
            return elm
    raise RuntimeError(f'Could not find an element with {expected}.')

friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 30},
    {'name': 'Anne', 'age': 27}
]

def get_friend_name(friend):
    return friend['name']

print(search(friends, 'Rolf', get_friend_name))