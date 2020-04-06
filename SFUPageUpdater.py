#!/usr/bin/python3
#Script to update html page on sfu sites
#Default updating one time in 3 min
#По умолчанию - скрипт посылает POST запрос на сайт один раз в 3 минуты

import requests
import datetime, time

LOGIN	 = str(input('\nEnter SFU-login: '))
PASSWORD = str(input('Enter SFU-password: '))
AUTH_URL = 'https://i.sfu-kras.ru'

DATA = {'AUTH_FORM':'Y',
	'TYPE':'AUTH',
	'backurl':'/index.php',
	'USER_LOGIN':LOGIN,
	'USER_PASSWORD':PASSWORD}

session = requests.Session()

def post_request():
	while True:
		SYSTEM_TIME  = datetime.datetime.now()
		CURRENT_TIME = SYSTEM_TIME.strftime('%X')
		if session.post(AUTH_URL, DATA):
			print(str(CURRENT_TIME + ' - REQUEST IS SENT!'))
		else:
			print('ERRORL REQUEST IS NOT SENT!')
		time.sleep(180)


if requests.get(AUTH_URL).status_code == 200:
	print('URL is true! Connecting... \n')
	post_request()
else:
	print('Ups...error((')


if __name__ == '__main__':
	post_request
