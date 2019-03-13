# Скачайте файл. В нём указан url адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк 
# в нём. Нужно результат (число кол-ва строк) записать в исходных файл.

import requests

with open('dataset_3378_2.txt') as a:
    line = a.readline().strip()
r = requests.get(line, verify=False)
result = len(r.text.splitlines())

with open('dataset_3378_2.txt', 'w') as r:
    r.write(str(result))

# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла. Первое слово в тексте последнего 
# файла: "We". Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. Все файлы располагаются в 
# каталоге по адресу: https://stepic.org/media/attachments/course67/3.6.3/ 

import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + '699991.txt')
next = r.text

count = 0
while next[:2] != "We":
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + next)
    next = r.text
    count += 1
    print(count)
print(next)

# Написать программу, которая каждый час проигрывает песню (всего 3 раза)

import webbrowser
import time

n = 1
while (n <= 3):
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=Qm4pP_gy2cU&index=2&list=LLNp6OVbHywyyhIWWKzgc8CA&t=0s")
    n = n+1

# Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля, находит для переданного ей на 
# стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.

import math
n = float(input())
print(math.pi*n*2)

# Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта выводить 
# не нужно). Не изменяйте порядок аргументов при выводе.

import sys
print(*sys.argv[1:])