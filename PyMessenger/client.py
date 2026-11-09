import socket # Импорт библиотеки для работы с сокетами (ip + port)
import threading # Импорт библиотеки для работы с многопоточностью
import os

os.system('cls' if os.name == 'nt' else 'clear')
banner = """
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
                print("\n[!] Собеседник отключился.")
                break
            # Зеленый цвет для друга, сброс цвета в конце (\033[0m)
            print(f"\n\033[92m[Собеседник]: {data.decode('utf-8')}\033[0m")
            print("Вы: ", end = "", flush = True) # Возвращаем приглашение ввода
        except:
            break

# Поднимаем клиент
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("[!] Не удалось подключиться.Убедитесь, что сервер запущен.")
        return

    print(f"[*] Подключено к серверу {HOST}:{PORT}.")

    # Запуск потока для приема сообщений

    thread = threading.Thread(target = receive_message, args = (client,), daemon=True)
    thread.start()

    # Цикл для отправки
    while True:
        try:
            msg = input("Вы: ")
            if msg.lower() == 'exit':
                break
            # Отправка сообщения на сервер
            client.sendall(msg.encode('utf-8'))
        except (KeyboardInterrupt, EOFError):
            break

    client.close()
    print("[*] Вы отключились.")

if __name__ == '__main__':
    start_client()