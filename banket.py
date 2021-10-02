"""
Задача №479. Транзитивность неориентированного графа
Напомним, что граф называется транзитивным, если всегда из того, что вершины u и v соединены ребром и вершины v и w
соединены ребром следует, что вершины u и w соединены ребром.
Проверьте, что заданный неориентированный граф является транзитивным.

Входные данные
Сначала вводятся числа n ( 1≤n≤100 ) – количество вершин в графе и m ( 1≤m≤n(n−1)/2 ) – количество ребер.
Затем следует m пар чисел – ребра графа.

Выходные данные
Выведите  «YES», если граф является транзитивным, и «NO» в противном случае.

Примеры
входные данные
5 1
2 5
выходные данные
YES

Пример работы кода
входные данные
5 5
1 3
1 4
5 2
3 2
4 2

После нормализации список 'l' будет равен
1 3
1 4
2 3
2 4
2 5

После заходим в 'func_1' и сортируем полученные данные на 'left' и 'right'
line = [1,3]
l=1 ; r=3
line = [1,4] # т.к '1' есть в 'l' '4' в 'r'
l=1 ; r=3,4
line = [2,3] # т.к '3' есть в 'r' '2' в 'l'
l=1,2 ; r=3,4
line = [2,4] # т.к '2' есть в 'l' '4' в 'r'
l=1,2 ; r=3,4,4
line = [2,5] # т.к '2' есть в 'l' '5' в 'r'
l=1,2 ; r=3,4,4,5

Теперь смотрим пересечение 2-х множеств 'l' и 'r'
Если пересечение равно нулю, тогда их можно рассадить
за два стола, иначе, нет.

func_2 нужно в некоторых случаях, когда у нас на входе два элемента
и обоих нет ещё ни в 'l' ни в 'r'
в func_1 мы их добавляем в конец, в список 'l', а потом их в самом конце проверяем,
иначе у нас есть два выбора куда сожать одного на леов другого на право или наоборот,
и наш выбор влияет на результат пока мы не расссмотрим все остальные пары.
"""


def func_1(line, di):
    di = {'left': [l[0][0]], 'right': [l[0][1]]}
    for i in line[1::]:
        if i[0] in di['right']:
            di['left'].append(i[1])
        elif i[0] in di['left']:
            di['right'].append(i[1])
        elif i[1] in di['right']:
            di['left'].append(i[0])
        elif i[1] in di['left']:
            di['right'].append(i[0])
        else:
            line.append(i)
    return line, di


def func_2(line, di):
    for i in line[M::]:
        if i[0] in di['right']:
            di['left'].append(i[1])
        elif i[0] in di['left']:
            di['right'].append(i[1])
        elif i[1] in di['right']:
            di['left'].append(i[0])
        elif i[1] in di['left']:
            di['right'].append(i[0])
        else:
            print('error')
    return line, di


N, M = map(int, input().split())
d = {'left': [], 'right': []}
l = []

for i in range(M):
    l.append(list(map(int, input().split())))
    l[i].sort()
l.sort()

l_new, d_new = func_1(l, d)
l, d = func_2(l_new, d_new)


for i in range(1, N + 1):
    if i not in (d['left'] and d['right']):
        d['left'].append(i)

d['left'].sort()
intersection = set(d['left']) & set(d['right'])

if len(intersection) == 0:
    print('YES')
    for i in set(d['left']):
        print(i, end=' ')
else:
    print('NO')
