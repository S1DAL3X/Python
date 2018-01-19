import random

print("\nПоиграем в BlackJack! ")
koloda = [2,3,4,6,7,8,9,10,11]
score = 0
diller = 0

choice = input("\nБерём карту? (Да/Нет)")

while choice != "Нет":
  card = random.choice(koloda)
	CardDiller = random.choice(koloda)
	print("\nВыпала карта " + str(card))
	score += card
	diller += CardDiller
	if score > 21:
		print("У Вас уже " + str(score) + " очко! Вы проиграли!")
		break
	elif score == 21:
		print("У Вас уже " + str(score) + " очко! ВЫ ВЫИГРАЛИ!!!")
		break
	else:
		print("У Вас уже " + str(score) + " очков")
		choice = input("Берём карту? (Да/Нет)")

# Проверка победили-ли мы диллера
if choice == "Нет" or choice == "нет":
	print("\nУ Вас уже " + str(score) + " очков!")
	print("У диллера " + str(diller) + " очков!")
	if score > diller:
		print("У Вас больше очков чем у диллера! ВЫ ВЫИГРАЛИ!!!")
	elif score == diller:
		print("У Вас и у диллера равное количество очков! НИЧЬЯ!")
	else:
		if diller > 21:
			print("У диллера перебор! ВЫ ВЫИГРАЛИ!")
		else:
			print("У вас меньше очков ,чем у диллера! Вы проиграли!")
# Created by Aleksey Sidorenko
