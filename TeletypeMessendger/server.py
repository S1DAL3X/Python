import socket                                                                   # Импорт библиотеки для работы с сокетами (ip + port)
import threading                                                                # Импорт библиотеки для работы с многопоточностью
from datetime import datetime
from colorama import Fore, Back, Style, init # Импорт библиотеки для работы с цветом в терминале
import telebanners
from telebanners import print_telebanner

init()  # Инициализация colorama

# Настройка сервера
HOST = '127.0.0.1'                                                              # IP-адрес сервера (поднимаем на локалхосте)
PORT = 12345                                                                    # Порт сервера

def handle_client(connection, address, other_connection=None):# Функция пересылки сообщений от одного клиента к другому
    # ПОЛУЧЕНИЕ ИМЕНИ ПЕРВЫМ СООБЩЕНИЕМ ОТ КЛИЕНТА
    username = None
    try:
        raw_name = connection.recv(1024).decode("utf-8")
        if not raw_name:
            connection.close()
            return

        if raw_name.startswith("NAME:"):
            username = raw_name.split(":", 1)[1].strip()
        else:
            username = f"User_{address[1]}" # Запасной вариант

        # УВЕДОМЛЕНИЕ КЛИЕНТОВ ПРИ ПОДКЛЮЧЕНИИ НОВЫХ КЛИЕНТОВ
        if other_connection:
            try:
                other_connection.sendall(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} {username} подключился к чату.".encode("utf-8"))
            except Exception as e:
                print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} Не удалось уведомить собеседника о подключении, ошибка {e}")

    except Exception as e:
        print(f"{Fore.YELLOW}[СИСТЕМА]{Style.RESET_ALL} Ошибка при получении имени: {e}")
        connection.close()
        return

    # ПЕРЕСЫЛКА СООБЩЕНИЯ ЧЕРЕЗ СЕРВЕР ОТ КЛИЕНТА К КЛИЕНТУ
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break

            now = datetime.now().strftime("%H:%M:%S")
            text = data.decode("utf-8")                                                     # Декодируем сообщение в строку перед форматированием
            formated_msg = f"{now}|{username}|{text}"                                       # Добавляем в сообщение время отправки (текущее время обработки)

            print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} {now} [{username}]: {text}")                           # Вывод переписки на сервере (лог)

            if other_connection:
                try:
                    other_connection.sendall(formated_msg.encode("utf-8"))          # Кодируем обратно и пересылаем данных другому клиенту
                except Exception as e:
                    print(f"{Fore.YELLOW}[СИСТЕМА]{Style.RESET_ALL} Ошибка отправки: {e}")

        except Exception as e:
            print(f"{Fore.YELLOW}[СИСТЕМА]{Style.RESET_ALL} Ошибка в цикле функции handle_client: {e}")
            break

    # СООБЩЕНИЕ ОБ ОТКЛЮЧЕНИИ КЛИЕНТА
    print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} Клиент {address} отключился.")
    if username and other_connection:
        try:
            other_connection.sendall(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} {username} покинул чат.".encode("utf-8"))
        except:
            pass

    connection.close()

def start_server():
    try:                                                                            # Поднимаем сервер
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  # создаем сокет (привязку сервер + порт)
        server.bind((HOST, PORT))                                                   # сервер слушает хост на порте
        server.listen(2)                                                            # сервер будет ожидать подключение 2х клиентов
        print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} Сервер запущен на {HOST}:{PORT}. Ожидание двух клиентов...")
        print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} Добро пожаловать на сервер Телетайп!\n")
    except:
        print("Ошибка поднятия сервера!")

    clients = []                                                                # создаем список клиентов
    while len(clients) < 2:
        connection, address = server.accept()
        clients.append((connection, address))
        print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} Подключился клиент: {address}")

    # Когда подключились оба клиента запускаем потоки для пересылки данных
    c1, a1 = clients[0]
    c2, a2 = clients[1]

    print(f"{Fore.BLUE}[СЕРВЕР]{Style.RESET_ALL} Оба клиента подключены. Можно общаться!")
    threading.Thread(target = handle_client, args=(c1, a1, c2), daemon = True).start()
    threading.Thread(target = handle_client, args=(c2, a2, c1), daemon = True).start()

    # Держим сервер запущенным
    while True:
        pass

if __name__ == '__main__':
    start_server()