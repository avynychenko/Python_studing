# Написать программу, которая каждый час проигрывает песню (всего 3 раза)

import webbrowser
import time

n = 1
while (n <= 3):
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=Qm4pP_gy2cU&index=2&list=LLNp6OVbHywyyhIWWKzgc8CA&t=0s")
    n = n+1

# Катя узнала, что ей для сна надо X минут. Катя ложится спать после полуночи в H часов и M минут. Помогите Кате определить, 
# на какое время ей поставить будильник, чтобы он прозвенел ровно через X минут после того, как она ляжет спать. Программа должна 
# выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.

sleep_min = int(input())
hours = int(input())
mins = int(input())
print(((hours * 60 + mins) + sleep_min) // 60)
print(((hours * 60 + mins) + sleep_min) % 60)

# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать 
# более B часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите 
# “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
# На вход программе в три строки подаются переменные в следующем порядке: A, B, H.

recom_sleep = int(input())
max_sleep = int(input())
actual_sleep = int(input())
if recom_sleep <= actual_sleep <= max_sleep:
    print ('Это нормально')
elif actual_sleep < recom_sleep:
    print ('Недосып')
else:
    print ('Пересып')

# Определить, является ли введенный год високосным или обычным

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print ('Високосный')
else:
    print ('Обычный')