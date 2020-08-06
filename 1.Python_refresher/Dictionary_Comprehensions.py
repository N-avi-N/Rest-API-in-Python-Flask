
users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'pass1234'),
    (2, 'Jose', '1234'),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping['Bob'])