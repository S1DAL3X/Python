#!/usr/bin/python3
#Script to update html page on sfu sites
#Default updating one time in 3 min
#По умолчанию - скрипт посылает POST запрос на сайт один раз в 3 минуты

import requests									#библиотека для обработки http запросов
import datetime, time								#библиотеки для работы с системным временем

LOGIN	 = str(input('\nEnter SFU-login: '))					#вводим СФУ логин
PASSWORD = str(input('Enter SFU-password: '))					#вводим СФУ пароль
AUTH_URL = 'https://i.sfu-kras.ru'						#ссылка на сайт

#данные (http-заголовки), которые будем посылать сайту
DATA = {'AUTH_FORM':'Y',
	'TYPE':'AUTH',
	'backurl':'/index.php',
	'USER_LOGIN':LOGIN,
	'USER_PASSWORD':PASSWORD}

#создали объект сессии (чтобы каждый раз отправлять на сайт одни и те же данные)
session = requests.Session()

#функция обработки запросов
def post_request():
	while True:
		SYSTEM_TIME  = datetime.datetime.now()				#системная дата
		CURRENT_TIME = SYSTEM_TIME.strftime('%X')			#системное время в читабельном формате
		if session.post(AUTH_URL, DATA):				#если запрос отправлен, то:
			print(str(CURRENT_TIME + ' - REQUEST IS SENT!'))	#вывести время + REQUEST IS SENT!
		else:								#иначе, 		
			print('ERRORL REQUEST IS NOT SENT!')			#вывести ERRORL REQUEST IS NOT SENT!
		time.sleep(180)							#цикл засыпает на три минусы(180 сек) и работает заново

#если запрос на сайт вернул код 200 (запрос успешно обработан), то запускаем функцию
if requests.get(AUTH_URL).status_code == 200:
	print('URL is true! Connecting... \n')
	post_request()
else:
	print('Ups...error((')

