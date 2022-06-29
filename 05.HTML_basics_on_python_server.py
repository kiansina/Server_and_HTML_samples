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
            AA='''
            <html>
            <head>
              <title>Gettin' Classy</title>  <!-- this part is the title on the tab of the browser -->
               <!-- Style part is css code and its comment is /* -->
              <style>
                /* I wish this were the default */
                body {
                  font-family: arial, sans-serif;
                }
                #first {
                  font-family: monospace;
                }
                #second {
                  color: green;
                }
                .morespace {
                  margin-left: 20px;
                  margin-right: 20px;
                }
                .shout {
                  text-transform: uppercase;
                }
                .loud {
                  color: red;
                }
                /* Paragraph tags within a tag with id */
                #third p {
                  background-color: yellow;
                }
              </style>
            </head>
            <body>
            <h1>Selecting and Styling Tags</h1>
            <div id="first">
            <p>
            To avoid putting too much into the
            <strong>style</strong> attribute,
            we can use the <strong>class</strong> and
            <strong>id</strong> attributes to style
            a subset of the tags.
            </p>
            <p class="morespace">
            An <strong>id</strong> tag must be unique
            through the document while the
            <strong>class</strong> tag can be used on
            many tags throughout the document.
            </div>
            <div id="second">
            <p>
            We can use the <strong>class</strong>
            <span class="shout">all</span> throughout
            the <span class="shout">entire</span>
            document.
            </p>
            <p class="morespace">
            It is <strong class="shout">very cool</strong>
            to use classes.  The can be used on any tag.
            </p>
            <p class="shout loud">
            A tag can have more than one class!.
            </p>
            </div>
            <div id="third">
            <p>
            You can even use a hierarchical selection string
            to style tags.
            </p>
            <p>
            In general it is nice to keep your HTML as clean
            and easily understood as possible as in this
            <a href="navbar.htm">
            &rArr; simple navigation bar
            </a> example.
            </p>
            </div>
            <!-- Ignore this for now :) -->
            <p style="border-style: none; position:fixed; bottom: 10px; right: 10px;">
            Go back to the
            <a href="index.htm">Starting page</a>.
            </p>
            <pre><code>if    i                     range</code></pre>
            <pre>if    i                     range</pre>
            <p>if    i                     range</p>
            <p><code>if    i                     range</code></p>
            </body>

            '''
            data += AA
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
