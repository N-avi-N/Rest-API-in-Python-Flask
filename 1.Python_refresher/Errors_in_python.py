
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be zero')

    return dividend / divisor

grades = []

print('Welcome to the grades average program.')

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print('There are no grades available yet')
else:
    print(f'The average grade is {average}.')
finally:
    print('Thank You !!!')


