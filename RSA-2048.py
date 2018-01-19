'''

NAME: RSA-2048
AUTHOR: S1DAL3X
VERSION: 1.0
PYTHON: 3.6.1

Before using need install rsa-module
pip install rsa

'''

import rsa

(public_key, private_key) = rsa.newkeys(2048)

#RSA worked only with bytes because utf-8
message = input('Please input your message: ')
message = message.encode('utf8')

#Encrypt message with public_key
crypto = rsa.encrypt(message, public_key)

#Decrypt message with private_key
message = rsa.decrypt(crypto, private_key)
print(message.decode('utf8'))