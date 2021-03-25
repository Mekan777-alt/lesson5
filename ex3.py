tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Сергей', 'Дмитрий', 'Борис']
klasses2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_gen(t, k):
    klas = k[:]
    if len(t) > len(k):
        for itm in range(len(t) - len(klas)):
            klas.append(None)
    for tutor, klass in zip(t, klas):
        yield tutor, klass


x = gen_gen(tutors, klasses)
y = gen_gen(tutors2, klasses2)
print(type(x))
print(*x)
print(type(y))
print(*y)
