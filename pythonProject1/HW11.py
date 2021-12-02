slovar1 = {1: 10, 2: 20}
slovar2 = {3: 30, 4: 40}
slovar3 = {5: 50, 6: 60}
obchslovar = dict()


def zapolnenieSlovar(n):
    obchslovar.update(n)


zapolnenieSlovar(slovar1)
zapolnenieSlovar(slovar2)
zapolnenieSlovar(slovar3)
print(obchslovar, '\n')

dannslovar = {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
              'emp3': {'name': 'Brad', 'salary': 6500}}
print(dannslovar['emp3'])
dannslovar['emp3']['salary'] = 8500
for i, j in dannslovar.items():
    print(i)
    for k, l in j.items():
        print(k, ':', l)
print()

slovarStud = dict()
h = 0
kolStudents = int(input('Количество студентов: '))
for i in range(kolStudents):
    print(i + 1, end='')
    student = input('-й студент: ')
    ball = float(input('Балл: '))
    for j in range(i + 1):
        slovarStud[student] = []
        for k in slovarStud:
            slovarStud[student] = ball
studSred = []
for i in slovarStud.values():
    h = h + i
sredBall = h / kolStudents
for i, j in slovarStud.items():
    if j > sredBall:
        studSred.append(i)

print('Средний балл: ', round(sredBall), ". Студенты с баллом выше среднего: ", sep='')
for i in studSred:
    print(i)

input()
