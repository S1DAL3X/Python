import os

directory = input('Enter a path to directory (use double slash) : ')
choice = input('Ypu want (E)ncode or (D)ecode files in this dir ? ')
files = os.listdir(directory)

for file in files:
    b = file.split('.')[-1]
    size = os.path.getsize(file)
    fileLength = str(hex(size))
    print(str(file))
    print(str(b))
    
    if choice == 'E':
        if b == 'doc':
            a = '0x11'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'txt':
            a = '0x12'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'exe':
            a = '0x13'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'avi':
            a = '0x14'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'jpg':
            a == '0x15'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'png':
            a = '0x16'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'docx':
            a = '0x17'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == 'bat':
            a = '0x18'
            os.rename(str(file), fileLength + '.' + str(a))
        else:
            pass
        print('Done !')
        
    elif choice == 'D':
        if b == '0x11':
            a = 'doc'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x12':
            a = 'txt'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x13':
            a = 'exe'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x14':
            a = 'avi'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x15':
            a = 'jpg'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x16':
            a = 'png'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x17':
            a = 'docx'
            os.rename(str(file), fileLength + '.' + str(a))
        elif b == '0x18':
            a = 'bat'
            os.rename(str(file), fileLength + '.' + str(a))
        else:
            pass
        print('Done !')
    
    else:
        pass
