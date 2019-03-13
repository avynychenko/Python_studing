# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на 
# стандартный вывод сводную таблицу результатов всех матчей. За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков

n = int(input())
p = []
for i in range(n):
    p += [input().split(';')]

d = {}
for j in p:
    if j[1] > j[3]:
        d.setdefault(j[0], []).append(3)
        d.setdefault(j[2], []).append(0)
    elif j[1] == j[3]:
        d.setdefault(j[0], []).append(1)
        d.setdefault(j[2], []).append(1)
    else:
        d.setdefault(j[0], []).append(0)
        d.setdefault(j[2], []).append(3)

for key, value in d.items():
    print((key + ':'), len(value), value.count(3), value.count(1), value.count(0), sum(value))

# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его 
# повторений (без учёта регистра) в формате "слово количество". Порядок вывода слов может быть произвольным, каждое уникальное 
# слово должно выводиться только один раз.

n = str(input()).lower().split()

d = {}
for i in n:
    d[i] = n.count(i)
for key, value in d.items():
    print(key, value)

# Напишите программу, которой на вход в первой строке подаётся число n — количество значений x, для которых требуется узнать 
# значение функции f(x), после чего сами эти n значений, каждое на отдельной строке. Программа должна после каждого введённого 
# значения аргумента вывести соответствующие значения функции f на отдельной строке. Для ускорения вычисления необходимо сохранять 
# уже вычисленные значения функции при известных аргументах.

n = int(input())

c = 0
arr = []
while c < n:
    m = int(input())
    arr.append(m)
    c += 1
d = {}
for i in range(n):
    if arr[i] in d:
        continue
    else:
        d[arr[i]] = f(arr[i])

for i in arr:
    if i in d:
        print(d[i])