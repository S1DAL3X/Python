#!/usr/bin/python3
#Script to update html page on sfu sites
#Default updating one time in (1 - 3) min
#По умолчанию - скрипт посылает POST запрос на сайт один раз в (1 - 4) минуты
import sys
import random
import colorama
import requests
import datetime, time
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

LOGIN    = str(input('\nEnter SFU-login: '))
PASSWORD = str(input('Enter SFU-password: '))
AUTH_URL = 'https://i.sfu-kras.ru'

DATA = {'AUTH_FORM':'Y',
        'TYPE':'AUTH',
        'backurl':'/index.php',
        'USER_LOGIN':LOGIN,
        'USER_PASSWORD':PASSWORD}

session = requests.Session()


def get_online_status():
        html_page       = session.post(AUTH_URL, DATA).text
        soup_object     = BeautifulSoup(html_page, 'lxml')
        user_online     = soup_object.find('span', id = 'user-name').text
        return str(user_online)


def post_request():
        try:
                print(Fore.GREEN + get_online_status() + ' - Online\n')
        except:
                print(Fore.RED + 'WRONG LOGIN OR PASSWORD! PLEASE CHECK IT.\n')
                sys.exit()
        while True:
                SYSTEM_TIME  = datetime.datetime.now()                                                                                                                                      
                CURRENT_TIME = SYSTEM_TIME.strftime('%X')                                                                                                                                   
                if session.post(AUTH_URL, DATA):                                                                                                                                            
                        print(Fore.GREEN + str(CURRENT_TIME + ' - REQUEST IS SENT!'))                                                                                                       
                else:                                                                                                                                                                       
                        print(Fore.RED + 'ERRORL REQUEST IS NOT SENT!')                                                                                                                     
                time_range = random.randint(60, 240)                                                                                                                                        
                time.sleep(time_range)                                                                                                                                                      
                                                                                                                                                                                            
                                                                                                                                                                                            
if requests.get(AUTH_URL).status_code == 200:
        print(Fore.CYAN + 'URL is online! Connecting... \n')
        if get_online_status != False:
                post_request()
        else:
                print('Error!')
else:
        print(Fore.RED + 'Ups...error ' + str(requests.get(AUTH_URL).status_code))
	
print(Style.RESET_ALL)
