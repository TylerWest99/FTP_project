#ftp_server

from socket import *
import sys
status = 1

HOST = 'localhost'
PORT = 1024

while(status == 1):

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        connection, address = s.accept()
        with connection:
            print('Connection initiated to (host, port): ', address)
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                connection.sendall(data)
