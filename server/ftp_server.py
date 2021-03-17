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

def retr(s):
    file = s.recv(1024)
    if(os.path.isfile(file)):
        with open(file, 'rb') as f:
            bytesSent = f.read()
            s.sendall(bytesSent)
    else:
        s.send("Error")


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
                #print(data)

                # list function
                if(data.decode() == 'L'):
                    list = listFunc(s)
                    connection.sendall(bytes(list, 'utf-8'))

                # store function
                if(data.decode() == 'S'):
                    print('S')

                # retrieve function
                if(data.decode() == 'R'):
                    print('R')
                    file = connection.recv(1024)
                    if(os.path.isfile(file)):
                        with open(file, 'rb') as f:
                            bytesSent = f.read()
                            connection.sendall(bytesSent)
                            f.close()
                    else:
                        connection.send("Error")

                if not data:
                    break
                
