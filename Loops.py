# Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна вывести фрагмент 
# таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].

a, b, c, d = int(input()), int(input()), int(input()), int(input())
for m in range(1):
    for z in range(c, d+1):
        print(" ", z, sep="\t", end="")
    print()
    for i in range(a, b+1):
        print(i, end='\t')
        for x in range(c, d+1):
            print(i * x, end='\t')
        print()

# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность 
# на стандартный вывод.  Кодирование осуществляется следующим образом: s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы 
# одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

a = input()

count = 1
string = str()

if len(a) == 1:
    print(a + "1")

for i in range(1, len(a)):
    if a[i] == a[i-1]:
      count += 1
      if i == len(a)-1:
          string += a[i] + str(count)
    else:
      string += a[i-1] + str(count)
      count = 1
      if i == len(a)-1:
          string += a[i] + str(count)
print(string)

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке. Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.

n = int(input())
i = 0
while i >= 0:
    if n < 10:
        i += 1
        n = int(input())
        continue
    if n > 100:
        break
    i += 1
    print(n)
    n = int(input())

# Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее арифметическое всех 
# чисел из отрезка [a;b], которые делятся на 3.

a, b = int(input()), int(input())

s = 0    # счетчик, который накапливает сумму
z = 0    # счетчик, который будет считать сколько чисел удовлетворяет условию
for i in range(a, b+1):
    if i % 3 == 0:
        s += i
        z += 1
print(s/z)

# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного 
# нуля выводит сумму полученных на вход чисел.

n = int(input())
s = 0
while n != 0:
    s += n
    n = int(input())
print(s)

# Напишите программу, которая помогает найти число: Программа должна считывать размеры команд (два положительных целых числа a и b, 
# каждое число вводится на отдельной строке) и выводить наименьшее число d, которое делится на оба этих числа без остатка.

a = int(input())
b = int(input())

r = 1
while r > 0:
    if r % a == 0 and r % b == 0:
        print(r)
        break
    r += 1

# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке.

s = input()

count = 0
for i in s.upper():
    if i == 'G' or i == 'C':
        count += 1
print(count/len(s) * 100) 