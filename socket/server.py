import socket

sock = socket.socket()                                                          #объект сокет с которым будем работать
sock.bind(('', 9090))                                               #хост и порт (хост не определен)
sock.listen(1)                                                                  #количество подключений

conn, addr = sock.accept()                                                     #принимаем подключение (новый сокет и адрес клиента) Именно этот сокет и будет использоваться для приема и посылке клиенту данных.

print('connected:' +  str(addr))

while True:                                                                     #пока есть подключение принимаем данные от клиента частями по 1024 байта(1Кб)
    data = conn.recv(1024)
    #if not data:                                                                #если данных нет - завершить прием
    #    break
    print(data)
    conn.send(b'Command ' + data.upper() + b' is complite!')                                                    #отправляем данные обратно клиенту в верхнем регистре

conn.close()
