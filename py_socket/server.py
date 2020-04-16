import socket

IP_ADDR = '0.0.0.0'
IP_PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((IP_ADDR, IP_PORT))

print('Server is UP on port ' + str(IP_PORT))

while True:
    data = s.recv(1024)
    print(data.decode('UTF-8'))
