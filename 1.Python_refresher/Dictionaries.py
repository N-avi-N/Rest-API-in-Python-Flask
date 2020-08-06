
friend_ages = {'Rolf':24, 'Adam':30, 'Anne':27}

friend_ages['Bob'] = 20

print(friend_ages)

friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 30},
    {'name': 'Anne', 'age': 27},
]

print(friends[1]['name'])

student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}
for k, v in student_attendance.items():
    print(f'Student Name {k}, and their attendance {v}')

print(sum(student_attendance.values()))