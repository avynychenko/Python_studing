# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в 
# этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое.
# Слова, написанные в разных регистрах, считаются одинаковыми.

with open('dataset_3363_3.txt') as aaa:
	z = " ".join(i.strip() for i in aaa)
	line = z.lower().split()

d = {}
for i in line:
	d[i] = line.count(i)

z = [k for k,v in d.items() if v == max(d.values())]
result = " ".join((min(z), str(d.get(min(z)))))


with open('dataset_3363_3.txt', 'w') as res:
	res.write(result)

# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём 
# предметам на отдельной строке, соответствующей этому абитуриенту. Также в конце файла, на отдельной строке, через пробел запишите 
# средние баллы по математике, физике и русскому языку по всем абитуриентам. 
# Данные предоставляюся в виде: Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

with open('dataset_3363_4.txt') as aaa:
	text = str()
	sum1 = 0
	sum2 = 0
	sum3 = 0
	count = 0
	for i in aaa:
		z = i.strip().split(';')
		avg = (int(z[1]) + int(z[2]) + int(z[3]))/3
		text += str(avg) + '\n'
		sum1 += int(z[1])
		sum2 += int(z[2])
		sum3 += int(z[3])
		count +=1
	text += ' '.join([str(sum1/count), str(sum2/count), str(sum3/count)])
with open('dataset_3363_4.txt', 'w') as ddd:
	ddd.write(text)

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