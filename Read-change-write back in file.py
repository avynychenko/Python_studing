# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и 
# производит обратную операцию, получая исходный текст. Запишите полученный текст в файл. 
# Пример: a3b4c2e10b1 - aaabbbbcceeeeeeeeeeb

with open('dataset_3363_2 (1).txt') as aaa:
	line = aaa.readline().strip()
num = []
string = []
str = []
count = 0
for i in range(len(line)):
	if line[i].isalpha():
		str += [line[i]]
	else :
		while i < len(line):
			if line[i].isdigit():
				num += [line[i]]
				count += 1
			else:
				if count == 1:
					string += int(num[0]) * str
				elif count == 2:
					string += int(num[0] + num[1]) * str
				count = 0
				num = []
				str = []
				break
			i += 1
	if count == 1:
		string += int(num[0]) * str
	elif count == 2:
		string += int(num[0] + num[1]) * str
victory = "".join(string)

with open ('dataset_3363_2 (1).txt', 'w') as result:
	result.write(victory)