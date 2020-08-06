
# "kwargs" is used to pass dictionary

def named(**kwargs):
    print(kwargs)

named(name='Bob', age=25)

details = {'name': 'Bob', 'age': 25}

named(**details)

def both(*args, **kwargs):
    print(args)
    print(kwargs)
    
both(1, 2, 3, name = 'Bob', age = 24)