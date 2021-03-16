#ftp_client
import socket
import sys
import os

HOST = '123456789'  # The server's hostname or IP address
PORT = 0       # The port used by the server

status = 1

# def connect(argv):
#     Host = arg1
#     PORT = arg2

host = ""
port = 0


user_input = input("> ")
ar1 = ""
ar2 = ""
ar3 = ""


counter = 1
spacesCounter = 0;
for i in range(len(user_input)):
    if(user_input[i] == " "):
        spacesCounter = spacesCounter + 1
if(spacesCounter == 2):
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

if (ar1 == "connect" or ar1 == "CONNECT" or ar1 == "C" or ar1 == "Connect" or ar1 == "c"):
    HOST = ar2
    PORT = ar3
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
    print("You have connected")
    status = 1;
    while(status == 1):
        print()
        print("What would you like to do? You can List, Retrieve, Store, or Quit")

        op = input("> ")

        if(op == "LIST" or op == "List" or op == "list" or op == "L" or op == "l"):
            print("The files in the current directory are...")
            print()
            # prints the files in the directory
            list = os.listdir('.')
            for i in list:
                print(i)

        if(op == "QUIT" or op == "Quit" or op == "quit" or op == "Q" or op == "q"):
            status = 0
            print("Disconnected")
else:
    print("Error in connecting")

    #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #    s.connect((HOST, PORT))
    #    val = input("Send or quit?")
    #    if(val == "Send" or val == "s"):
    #        s.sendall(b'1')
    #        data = s.recv(1024)
    #    if(val == "Quit" or val == "q"):
    #        status = 0
    #print('Received', repr(data))
