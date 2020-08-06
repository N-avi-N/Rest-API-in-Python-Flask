friends = ['Rolf', 'Bob']
abroad = ['Rolf', 'Bob']

print(friends == abroad)
print(friends is abroad, '\n')


friends = ['Rolf', 'Bob']
abroad = friends

print(friends == abroad)
print(friends is abroad, '\n')

friends = ['Rolf', 'Bob']
abroad = ['Bob', 'Rolf']

print(friends == abroad)
print(friends is abroad, '\n')