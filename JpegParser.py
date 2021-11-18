import os, shutil
from os import path

path_folder = input("Enter path: ")                     # Вводить по примеру "C:/Users/User/Desktop/fodler_name"
path2_folder = input("Enter name of dir to copy: ")     # Ввести имя для папки копирования (без пробелов и русских символов), папка создастся в path_folder
ext = [".jpeg", ".jpg", ".png", ".img"]                 # Словарь расширений для парсинга 

os.chdir(path_folder)
os.mkdir(path2_folder)


for file_name in os.listdir():
    if os.path.splitext(file_name)[1] in ext:
        shutil.copy(file_name, path2_folder)
    else:
        pass
        
