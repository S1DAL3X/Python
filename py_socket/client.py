import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

SERVER_ADDR = str(input('Server IP:   '))
SERVER_PORT = int(input('Server PORT: '))
USER_NAME   = str(input('Your name:   '))

while True:
        message = input('\nMessage: ')
        message = str(USER_NAME + ': ' + message)
        sock.sendto(message.encode('UTF-8'), (SERVER_ADDR, SERVER_PORT))
sock.close()
