import os, sys, time
import zipfile                      #Модуль zipfile для работы с архивацией
import datetime                     #Модуль datetime для работы с датой системы


PATH = os.getcwd()                            #Получение текущего пути скрипта
CONTENT = os.listdir(PATH)                    #Получение списка файлов
date_now = str(datetime.datetime.now())[0:10] #Получение текущей даты


#Функция Archiver для архивации содержимого дериктории
def archiver():
    archive_name = f"\Archive_{date_now}.zip"
    archive_file = zipfile.ZipFile(str(PATH) + str(archive_name), "w")

    for folder, subfolders, files in os.walk(PATH):

        for file in files:

            if str(file)[0:7] == "Archive":
                timer_check(file)
                pass
            else:
                archive_file.write(os.path.join(folder, file), os.path.join(folder, file), compress_type = zipfile.ZIP_DEFLATED)

    archive_file.close()

    
#Функция Timer_Check для проверки даты создания файла
def timer_check(file):
    
    current_time = time.time()
    creation_time = os.path.getctime(file)

    if(current_time - creation_time) // (24*3600) >= 7:
        deleter(file)
    
#Функция Deleter_Archive для удаления устаревших архивов (дата создания которых больше на 7 дней от текущей даты)
def deleter(file):
    os.unlink(file)
    
    
#Запуск основных функций
def main():
    archiver()
    
    
if __name__ == "__main__":
    main()
