import socket

USER_NAME    = str(input('Your name:   '))
SERVER_ADDR  = str(input('Server IP:   '))
SERVER_PORT  = int(input('Server PORT: '))
SOCK_INFO    = '\nAddress: ' + SERVER_ADDR + ', Port: ' + str(SERVER_PORT) + '\n'

while True:
    message = input('Enter message: ')
    message = str(USER_NAME + ": " + message)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_ADDR, SERVER_PORT))
    sock.send(message.encode('UTF-8'))
    sock.send(SOCK_INFO.encode('UTF-8'))
    
sock.close()
