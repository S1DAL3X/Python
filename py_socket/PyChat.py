import socket
from threading import Thread

def server_side():
    SERVER_ADDR = '0.0.0.0'
    SERVER_PORT = int(input('SERVER_PORT = '))
    
    sock_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_serv.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock_serv.bind((SERVER_ADDR, SERVER_PORT))

    print('Server side is UP !')

    while True:
        data = sock_serv.recv(4096)
        print(data.decode('UTF-8'))
        
    sock_serv.close()

def client_side():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    USER_NAME   = str(input('Enter Your name: '))
    SERVER_ADDR = str(input('SERVER_HOST = '))
    SERVER_PORT = int(input('SERVER_PORT = '))
    print('\n')
    
    while True:
        message = input('Message: ')
        message = str(USER_NAME + ':  ' + message)
        sock_client.sendto(message.encode('UTF-8'), (SERVER_ADDR, SERVER_PORT))

    sock_client.close()

def main():
    print('Welcome to PyChat! ')
    th_server, th_client = Thread(target = server_side), Thread(target = client_side)
    th_server.start(), th_client.start()
    th_server.join(),th_client.join()

if __name__ == '__main__':
    main()
