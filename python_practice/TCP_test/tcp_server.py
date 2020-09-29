"""
About this file
    Filename: tcp_server.py
    Summary: A server-side script for a simple TCP communication. 

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
BUFFER_SIZE = 20

# Socket setting
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1) # Wait for the possible 'hello!' from any clients

# If connected, show info
connection, addr = server_socket.accept()
print("Connection address: ", addr)

# Repeat the communication
while 1:

    # Receive the request and terminate the server-side connection
    # if the client sent an empty stirng as the request
    REQ = connection.recv(BUFFER_SIZE)
    if not REQ:
        print("Client request nothing;\nterminating communication")
        break
    print("Received request: ", REQ.decode())

    # Determine the message according to the request
    if REQ.decode() == "a":
        MESSAGE = "A"
    elif REQ.decode() == "b":
        MESSAGE = "B"
    else:
        MESSAGE = input("What to send: ")

    # Send the message and terminate the server-side connection
    # if the server sent an empty string as the message
    connection.send(MESSAGE.encode())
    if not MESSAGE:
        print("Server sent nothing;\nterminating communication")
        break
    else:
        print("Sent message: ", MESSAGE)

# Clean up
connection.close()
server_socket.close()
