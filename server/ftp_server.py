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
            while status == 1:
                data = connection.recv(1024)
                #print(data)

                #close server
                if(data.decode() == "q"):
                    quit()

                # list function
                if(data.decode() == 'L'):
                    list = listFunc(s)
                    connection.sendall(bytes(list, 'utf-8'))

                # store function
                if(data.decode() == 'S'):
                    #print('S')
                    fileNameBytes = connection.recv(1024)
                    fileName = fileNameBytes.decode()
                    f = open('new_'+fileName,'wb')
                    data = connection.recv(1024)
                    f.write(data)
                    f.close()

                # retrieve function
                if(data.decode() == 'R'):
                    #print('R')
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
                
