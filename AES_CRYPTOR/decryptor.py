#!/usr/bin/python

import os, random, struct, hashlib
from Crypto.Cipher import AES


def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

key = hashlib.sha256("China2019").digest()
#filename = raw_input("Enter filename for decrypt: ")
#decrypt_file(key, filename)
aes_files = []
for file in os.listdir(os.getcwd()):
    if file.split(".")[-1] == 'enc':
	decrypt_file(key, file)
    else:
	pass
