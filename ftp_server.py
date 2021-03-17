#ftp_server

from socket import *
import sys
import os
status = 1

HOST = 'localhost'
PORT = 1024

def listFunc(s):
    # gets a list of files in the directory
    list = os.listdir('.')
    newList = ""
    for i in list:
        newList = newList + i + " "
    print(newList)
    return newList

while(status == 1):

    with socket(AF_INET, SOCK_STREAM) as s:
        print("Server started!")
        s.bind((HOST, PORT))
        s.listen()
        connection, address = s.accept()
        with connection:
            print('Connection initiated!')
            while True:
                data = connection.recv(1024)
                print(data)

                # list func support
                list = listFunc(s)
                # logic for list
                if(data.decode() == 'L'):
                    connection.sendall(bytes(list, 'utf-8'))
                if not data:
                    break
                #connection.sendall(bytes("NOPE!", 'utf-8'))
