def hello():
    print('Hello World!')


hello()


def add(x, y=8):
    result = x + y
    print(result)


add(5)

# Lambda Function
add_lambda = lambda x, y: x + y
print(add_lambda(5, 5))

print((lambda x, y: x * y)(8, 9))

seq = [1, 2, 3, 4]
doubled = [(lambda x: x*2)(i) for i in seq]
print(doubled)

seq = [1, 2, 3, 4]
doubled = [(lambda x: x*2)(i) for i in seq]

def dou(x):
    return x * 2

doub = list(map(dou, seq))
print(doub)

doub = list(map((lambda x: x*2), seq))
print(doub)