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

# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой 
# длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт 
# строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

n, p, k, m = list(input()), list(input()), list(input()), list(input())

d = {}
count = 0
while count < len(n):
    d[n[count]] = p[count]
    count += 1
res = str()
for i in k:
    res += d.get(i)
res2 = str()
print(res)
for j in m:
    for key, value in d.items():
        if value == j:
            res2 += key
print(res2)

# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов. Напишите программу, которая прочитает этот 
# файл и подсчитает для каждого класса средний рост учащегося. Файл состоит из набора строк, каждая из которых представляет собой 
# три поля: Класс Фамилия Рост.Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с 
# первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.

with open('dataset_3380_5.txt') as file:
    pupils = []
    for i in file:
        pupils += [i.strip().split('\t')]
d = {}
for i in range(1, 12):
    d[i] = []
for j in pupils:
    d[int(j[0])].append(int(j[2]))

for k in d:
    if d[k] != []:
        d[k] = sum(d[k])/len(d[k])
    else:
        d[k] = '-'
for key, value in d.items():
    print(key, value, end = '\n')

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

# Программе подаётся на вход число команд n, которые нужно выполнить черепашке, после чего n строк с самими командами, где первое 
# слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное расстояние в сантиметрах, 
# которое должна пройти черепашка. Нужно написать программу, которая выведет точку, в которой окажется черепашка после всех команд. 
# Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на 
# север — вторую. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. 

n = int(input())
list = []
d = {}
for i in range(n):
    list += [input().split(" ")]
for j in list:
    d.setdefault(j[0], []).append(int(j[1]))

x = 0
y = 0
for k in d:
    if k == 'север':
        y += sum(d[k])
    elif k == 'запад':
        x -= sum(d[k])
    elif k == 'юг':
        y -= sum(d[k])
    elif k == 'восток':
        x += sum(d[k])
print(x, y)