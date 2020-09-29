"""
About this file
    Filename: tcp_client.py
    Summary: A client-side script for a simple TCP communication.

Description:
    When the client sends a request (= send a string) to the server,
    the server sends a message (= send a string) to the client as a reply.
    If the request is 'a' or 'b', the message is automatically
    determined as 'A' or 'B' respectively and automatically sent.
    Else if the request is an empty string, the communication is terminated.
    Else if the request is other than 'a' or 'b' or an empty string,
    the user manually determines the message and send it.

How to run:
    0. Make sure the value of TCP_IP and TCP_PORT
        is identical in tcp_server.py and tcp_client.py.
    1. Run tcp_server.py.
    2. Run tcp_client.py.
    3. In the client's console, type in your request string
        ('a' or 'b' or an empty string or anyting else.)
    4. The server's console shows the received request.
    5. Write a message if the request wasn't 'a', 'b', or an empty string.
    6. Repeat the communication as long as you want.
    7. Send an empty string as a request if you want to finish communication.
"""

import socket

# Connection info
TCP_IP = '127.0.0.5'
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Socket setting
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

# Repeat the communication
while 1:

    # Send the request and terminate the client-side connection
    # if the client sent an empty string as the request
    REQ = input("What to request: ")
    if not REQ:
        print("Client request nothing;\nterminating communication")
        break
    client_socket.send(REQ.encode())

    # Receive the message and terminate the client-side connection
    # if the server sent an empty string as the message
    MESSAGE = client_socket.recv(BUFFER_SIZE)
    if not MESSAGE:
        print("Server sent nothing;\nterminating communication")
        break
    else:
        print("Received data: ", MESSAGE.decode())

# Clean up
client_socket.close()
