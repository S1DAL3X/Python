import socket                   # Импорт библиотеки для работы с сокетами (ip + port)
import threading                # Импорт библиотеки для работы с многопоточностью

# Настройка сервера
HOST = '127.0.0.1'              # IP-адрес сервера (поднимаем на локалхосте)
PORT = 12345                    # Порт сервера
banner = """
    ____           __  ___                                         
   / __ \__  __   /  |/  /__  _____________  ____  ____ ____  _____
  / /_/ / / / /  / /|_/ / _ \/ ___/ ___/ _ \/ __ \/ __ `/ _ \/ ___/
 / ____/ /_/ /  / /  / /  __(__  |__  )  __/ / / / /_/ /  __/ /    
/_/    \__, /  /_/  /_/\___/____/____/\___/_/ /_/\__, /\___/_/     
      /____/                                    /____/    
                            SERVER
      """

def handle_client(connection, address, other_connection):                       # Функция пересылки сообщений от одного клиента к другому
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            print(f"[MSG] Получено от {address}:  {data.decode('utf-8')}")      # Вывод переписки на сервере
            if other_connection:
                other_connection.sendall(data)                                  # Пересылка полученных данных другому клиенту
        except:
            break

    print(f"[-] Клиент {address} отключился.")
    connection.close()

def start_server():                                                             # Поднимаем сервер
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  # создаем сокет (привязку сервер + порт)
    server.bind((HOST, PORT))                                                   # сервер слушает хост на порте
    server.listen(2)                                                            # сервер будет ожидать подключение 2х клиентов
    try:
        print(banner)
    except SyntaxWarning:
        pass
    print(f"[*]  Сервер запущен на {HOST}:{PORT}. Ожидание двух клиентов...")

    clients = []                                                                # создаем список клиентов
    while len(clients) < 2:
        connection, address = server.accept()
        clients.append((connection, address))
        print(f"[+] Подключился клиент: {address}")

    # Когда подключились оба клиента запускаем потоки для пересылки данных
    c1, a1 = clients[0]
    c2, a2 = clients[1]

    print("[*] Оба клиента подключены. Можно общаться!")
    threading.Thread(target = handle_client, args=(c1, a1, c2), daemon = True).start()
    threading.Thread(target = handle_client, args=(c2, a2, c1), daemon = True).start()

    # Держим сервер запущенным
    while True:
        pass

if __name__ == '__main__':
    start_server()