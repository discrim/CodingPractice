"""
AUTHOR: June Park, junkeunp@umich.edu
FILENAME: tcp_simple_socket.py

DESCRIPTION:
This is a simple server for TCP communication.
If the server connects to a client, it prints a success message.
"""

import socket

# Connection info
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

# Socket setting
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1) # Wait for the possible 'hello!' from any clients

# If connected, show info
connection, addr = server_socket.accept()
print("Connection address: ", addr)

#REQ = connection.recv(BUFFER_SIZE)

# Clean up
connection.close()
server_socket.close()
