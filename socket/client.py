import socket

sock = socket.socket()                                                     #объект сокет с которым будем работать

sock.connect(('192.168.1.22', 9090))                                          #подключаемся к localhost по порту 9090

while True:
    message = input('message: ')
    sock.send(bytes(message, 'utf8'))
    data = sock.recv(1024)
    print(data)
