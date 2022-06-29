import socket
mysock =socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This creates the socket who lives in my computer. (Creates phone)
mysock.connect(('data.pr4e.org', 80)) # Like : Dial the phone
# It includes the Domain name, and a port in that domain name
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
