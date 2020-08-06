def multiply(*args):
    print(args)
    tot = 1
    for arg in args:
        tot *= arg

    return tot

print(multiply(1, 2, 3))

def add(x, y):
    return x + y

nums = [1, 3]
print(add(*nums))

nums = {'x': 15, 'y': 25}
print(add(*nums.values()))
print(add(**nums))

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return add(*args)
    else:
        return 'No valid input given to apply'

print(apply(2, 3, operator='+'))