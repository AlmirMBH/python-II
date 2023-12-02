# tuple is a collection that is ordered and unchangeable
# used to group together related data

student = ('Almir', 44, 'male')

print(student.count(44))
print(student.index('male'))

if 'Almir' in student:
    for item in student:
        print(item)
