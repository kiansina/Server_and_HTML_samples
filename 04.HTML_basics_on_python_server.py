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
            AA='''<html><h1>This is me </h1><p>You can add a style like <strong>bold</strong> to some text by enclosing it in
             the <em>appropriate </em>tag</p><body>Hello World</body><p>Hello World</p><img src="1.png"></html>\r\n\r\n
            '''
            data += AA
            data += "<html><p>less than &lt; greater than &gt; ampersand &amp; ampersand inception &amp;amp; semicolon jsut works ; money characters &pound; &euro; &yen; math characters &sum; &forall; &isin; arrows: &larr; &uarr; &rarr; &darr;</p></html>"
            data += "<html> the special<!-- Ignore this for now :) --> characters can be in links: <a href='lists.htm'>&spades;&clubs;&hearts;&diams;</a></p></html>"
            data += "<html> if you want go and <a href='http://www.google.com/'> search</a></html>"
            data += "<html> make image clickable <a href= http://www.google.com><img src='1.png'></a></html>"
            data += "<html>making a list (List parameters don't have to be within parameters, but this helps to distant them in a beautiful way.)<ul><li><p>This pages</p></li><li><p>That pages</p></li></ul></html>"
            data += "<html><table><tr><th>make</th><th>Model</th><th>Mileage</th></tr><tr><td>Ford</td><td>Edge</td><td>10348</td></tr></table></html>"
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
