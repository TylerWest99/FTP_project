#ftp_client

from socket import *
import sys
import os
import time

status = 1

buf_size = 1024

user_input = input("> ")
ar1 = ""
ar2 = ""
ar3 = ""

counter = 1
space_counter = 0

for i in range(len(user_input)):
    if(user_input[i] == " "):
        space_counter = space_counter + 1
if(space_counter == 2):
    for i in range(len(user_input)):
        if(user_input[i] != " " and counter == 1):
            ar1 = ar1 + user_input[i]
        if(user_input[i] != " " and counter == 2):
            ar2 = ar2 + user_input[i]
        if(user_input[i] != " " and counter == 3):
            ar3 = ar3 + user_input[i]
        if(user_input[i] == " "):
            counter = counter + 1
    ar3 = int(ar3)

# connect function
if (ar1.strip().upper() == "CONNECT" or ar1.strip().upper() == "C"):
    HOST = ar2
    PORT = ar3

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("You have connected to\nHOST: %s\nPORT: %s" % (HOST, PORT))
        status = 1

        # loop once connected
        while(status == 1):
            print()
            print("What would you like to do? You can List, Retrieve, Store, or Quit")

            # operation code
            op = input("> ")
            op2 = op.split()

            # list function
            if(op.strip().upper() == "LIST" or op.strip().upper() == "L"):
                s.sendall(bytes("L", 'utf-8'))
                list = s.recv(buf_size)
                list = list.decode();
                print("The files in the current directory are...\n")
                print("_________________________________________\n")
                # prints the files in the directory
                list = list.split()
                for i in list:
                    print(i)
                print("_________________________________________\n")

            # store function
            if(op2[0].upper() == "STORE" or op2[0].upper() == "S"):
                print('file sent')
                s.sendall(bytes("S", 'utf-8'))
                fileName = op2[1]
                s.sendall(bytes(op2[1], 'utf-8'))
                if(os.path.isfile(fileName)):
                    with open(fileName, 'rb') as f:
                        bytesSent = f.read()
                        bytesSent = bytesSent.decode()
                        s.sendall(bytes(bytesSent, 'utf-8'))
                        f.close()
                else:
                    s.send(bytes("Error", 'utf-8'))

            # retrieve function
            if(op2[0].upper() == "RETRIEVE" or op2[0].upper() == "R"):
                print('file recieved')
                s.sendall(bytes("R", 'utf-8'))
                fileName = op2[1]
                s.send(bytes(fileName, 'utf-8'))
                f = open('new_'+fileName,'wb')
                data = s.recv(buf_size)
                f.write(data)
                f.close()

            # quit function
            if(op.strip().upper() == "QUIT" or op.strip().upper() == "Q"):
                s.sendall(bytes("q", 'utf-8'))
                status = 0
                s.close()
                print("Successfully disconnected from the server")
else:
    print("Error in initial connection")
