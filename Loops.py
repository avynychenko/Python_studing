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