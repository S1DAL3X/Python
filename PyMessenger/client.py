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
      """
# Настройка сервера
HOST = '127.0.0.1'
PORT = 12345


def receive_message(sock):
    # Фоновая функция (поток) для получения сообщений
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                sys.stdout.write("\r\033[K")                        # Стираем строку
                print(f"[!] Собеседник отключился...")
                break

            now = datetime.now().strftime("%H:%M:%S")               #Вычисляем текущее время в функции приема (показа) сообщений
            text = data.decode("utf-8")

            if "|" in text:
                time_part, msg_part = text.split("|", 1)
                sys.stdout.write("\r\033[K")
                print(f"{Fore.GREEN}[{time_part}]{Style.RESET_ALL} {Fore.MAGENTA}Собеседник: {Style.RESET_ALL}{msg_part}")
            else:
                sys.stdout.write("\r\033[K")
                print(f"{Fore.MAGENTA}Собеседник: {Fore.RESET_ALL} {text}")

            sys.stdout.write(f"{Fore.GREEN}[{now}]{Style.RESET_ALL} {Fore.CYAN}Вы: {Style.RESET_ALL}")                                # Возвращаем приглашение ввода
            sys.stdout.flush()
        except:
            break


# Поднимаем клиент
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем соединение IP:PORT по протоколу TCP

    print(banner)

    try:
        client.connect((HOST, PORT))
        print(f"[*] Подключено к серверу {HOST}:{PORT}.")
    except ConnectionRefusedError:
        print("[!] Не удалось подключиться.Убедитесь, что сервер запущен.")
        return

    # Запуск потока для приема сообщений
    thread = threading.Thread(target = receive_message, args = (client,), daemon=True)
    thread.start()

    while True:
        try:
            now = datetime.now().strftime("%H:%M:%S")
            msg = input(f"{Fore.GREEN}[{now}]{Style.RESET_ALL} {Fore.CYAN}Вы: {Style.RESET_ALL}")
            if msg.lower() == "exit":
                break
            if not msg.strip():
                continue

            sys.stdout.write("\r\033[K")                                # Стираем строку
            client.sendall(msg.encode('utf-8'))

        except (KeyboardInterrupt, EOFError):
            break

    client.close()
    print(f"[*] Вы отключились.")


if __name__ == '__main__':
    start_client()