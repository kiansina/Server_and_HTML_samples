from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000)) #we use try because if we run it two times it will blow up. Once a program uses 9000 port, it is impossible for the other program to use the same port
        serversocket.listen(5) # It says to Operating system that if I'm busy handling one phone call, you can hold on to four more
        while(1) :
            (clientsocket, address) = serversocket.accept() #It makes the server ready to be called
            # From this part of code runs just if some client program wants to connect our server.
            #Then after connection succedd based on http protocol client should first talks. so we recieve.
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0) : print(pieces[0])
            data = "HTTP/1.1 200 ok\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            # As the protocol says so as soon as we send the data we close the connection
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt :
        print("\nShutting down ...\n");
    except exception as exc:
        print("Error:\n");
        print(exc)
    serversocket.close()

print('Access http://localhost:9000')
createServer()
