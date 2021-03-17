#ftp_client

from socket import *
import sys
import os

status = 1

host = ""
port = 0

user_input = input("> ")
ar1 = ""
ar2 = ""
ar3 = ""

counter = 1
spacesCounter = 0

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

if (ar1.strip().upper() == "CONNECT" or ar1.strip().upper() == "C"):
    HOST = ar2
    PORT = ar3

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("You have connected to\nHOST: %s\nPORT: %s" % (HOST, PORT))
        status = 1

    while(status == 1):
        print()
        print("What would you like to do? You can List, Retrieve, Store, or Quit")

        op = input("> ")

        if(op.strip().upper() == "LIST" or op.strip().upper() == "L"):
            print("The files in the current directory are...\n")
            print("_________________________________________\n")
            # prints the files in the directory
            list = os.listdir('.')
            count = 0
            for i in list:
                print(i)
                count += 1
            print("Number of files found: ", count)
            print("_________________________________________\n")

        if(op.strip().upper() == "QUIT" or op.strip().upper() == "Q"):
            status = 0
            s.close()
            print("Disconnected")
else:
    print("Error in connecting")
