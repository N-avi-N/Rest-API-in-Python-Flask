l = ['Bob', 'Rolf', 'Anne']
t = ('Bob', 'Rolf', 'Anne')
s = {'Bob', 'Rolf', 'Anne'} #same as list but does not have order and duplicates, cannot access values by subscript

l.append('a')
print(l)

l.remove('a')
print(l)

s.add('a')
print(s)

friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

local_friends = friends.difference(abroad)

print('Local friends are {}'.format(local_friends))

local = {'Rolf'}
friends_all = local.union(abroad)

print('Name of all friends : {}'.format(friends_all))

arts = {'a', 'b', 'c', 'd'}
science = {'c', 'd', 'e'}

both = arts.intersection(science)

print('Students with both arts and science are : {}'.format(both))