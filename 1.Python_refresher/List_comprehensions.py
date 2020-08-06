

numbers = [1, 3, 5]
double = [i*2 for i in numbers]

print(double)


friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = [friend for friend in friends if friend.startswith('S')]
print(starts_s)