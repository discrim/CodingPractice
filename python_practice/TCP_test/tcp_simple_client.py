"""
AUTHOR: June Park, junkeunp@umich.edu
FILENAME: tcp_simple_socket.py

DESCRIPTION:
This is a simple client for TCP communication.
If the client connects to a server, the client terminates without errors.
"""

import socket

# Connection info
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Socket setting
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

client_socket.close()
