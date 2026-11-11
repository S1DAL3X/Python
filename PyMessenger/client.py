import socket       # Импорт библиотеки для работы с сокетами (ip + port)
import threading    # Импорт библиотеки для работы с многопоточностью
import os, sys
from datetime import datetime                # Импорт библиотеки для показа времени отправки сообщения
from colorama import Fore, Back, Style, init # Импорт библиотеки для работы с цветом в терминале

init()                                                      # Инициализация colorama
banner = r"""
    ____           __  ___                                         
   / __ \__  __   /  |/  /__  _____________  ____  ____ ____  _____
  / /_/ / / / /  / /|_/ / _ \/ ___/ ___/ _ \/ __ \/ __ `/ _ \/ ___/
 / ____/ /_/ /  / /  / /  __(__  |__  )  __/ / / / /_/ /  __/ /    
/_/    \__, /  /_/  /_/\___/____/____/\___/_/ /_/\__, /\___/_/     
      /____/                                    /____/    
                            CLIENT
                            
Справка: для выхода из чата введите \exit
      """
# Настройка сервера
HOST = '127.0.0.1'
PORT = 12345

# ФУНКЦИЯ (ПОТОК) ДЛЯ ПОЛУЧЕНИЯ СООБЩЕНИЙ
def receive_message(sock):
    while True:
        try:
            data = sock.recv(1024)                                  # Ожидание получения данных по 1024 байт
            if not data:
                sys.stdout.write("\r\033[K")                        # Стираем строку
                print(f"[!] Собеседник отключился...")              # Если данных нет вывод сообщения об отключении собесденика
                break                                               # Завершение цикла

            now = datetime.now().strftime("%H:%M:%S")               # Вычисляем текущее время в функции приема (показа) сообщений
            text = data.decode("utf-8")                             # Раскодировка полученных данных (если они есть)

            # СИСТЕМНОЕ СООБЩЕНИЕ О ПОДКЛЮЧЕНИИ\ОТКЛЮЧЕНИИ
            if text.startswith("[SYS]|"):
                _, msg = text.split("|", 1)
                sys.stdout.write("\r\033[K")
                print(f"{Fore.YELLOW}[SYS] {msg}{Style.RESET_ALL}")

            # ОБЫЧНОЕ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЕЙ: ВРЕМЯ|ИМЯ|ТЕКСТ
            elif "|" in text:
                parts = text.split("|", 2) # Максимум 3 части
                if len(parts) == 3:
                    time_part, name_part, msg_part = parts
                    sys.stdout.write("\r\033[K")
                    print(f"{Fore.GREEN}[{time_part}]{Style.RESET_ALL} {Fore.MAGENTA}{name_part}:{Style.RESET_ALL} {msg_part}")
                else:
                    print(text)
            else:
                print(text)

            sys.stdout.write(f"{Fore.CYAN}Вы: {Style.RESET_ALL}")
            sys.stdout.flush()
        except:
            break

# ФУНКЦИЯ ПОДНЯТИЯ КЛИЕНТА
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем соединение IP:PORT по протоколу TCP
    print(banner)

    try:
        client.connect((HOST, PORT))
        print(f"[*] Подключено к серверу {HOST}:{PORT}.")

        # ЗАПРОС ИМЕНИ ПОЛЬЗОВАТЕЛЯ ПОСЛЕ УСПЕШНОГО ПОДКЛЮЧЕНИЯ К СЕРВЕРУ
        username = input("Введите Ваше имя: ").strip()
        if not username:
            username = "Аноним"
        client.sendall(f"NAME:{username}".encode("utf-8"))
        print(f"[*] Вы вошли как {username}.")

    except ConnectionRefusedError:
        print("[!] Не удалось подключиться.Убедитесь, что сервер запущен.")
        return

    # Запуск потока для приема сообщений
    thread = threading.Thread(target = receive_message, args = (client,), daemon=True)
    thread.start()

    while True:
        try:
            msg = input(f"{Fore.CYAN}Вы: {Style.RESET_ALL}")
            if msg.lower() == "\exit":
                break
            if not msg.strip():
                continue

            sys.stdout.write("\033[F\033[K")                                # Стираем строку
            sys.stdout.flush()

            now = datetime.now().strftime("%H:%M:%S")
            print(f"{Fore.GREEN}[{now}]{Style.RESET_ALL} {Fore.CYAN}Вы:{Style.RESET_ALL} {msg}")

            client.sendall(msg.encode("utf-8"))

        except (KeyboardInterrupt, EOFError):
            break

    client.close()
    print(f"[*] Вы отключились.")

if __name__ == '__main__':
    start_client()