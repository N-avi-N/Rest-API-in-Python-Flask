
number = 7
user_input = input("Would you like to play? (Y/n)").lower()

while True:
    user_number = int(input('Guess our number: '))

    if user_input == 'n':
        break

    if user_number == number:
        print('You guessed correctly!')
        break
    elif number - user_number in (1, -1):
        print('You were off by one.')
    else:
        print("Sorry, it's wrong!")

