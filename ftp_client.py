#ftp_client
import socket
import sys
import ftplib

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

status = 1

# def connect(argv):
#     Host = arg1
#     PORT = arg2


while(status == 1):

    user_input = input("> ")

    if (user_input == "CONNECT"):
        host = sys.argv[1]
        port = sys.argv[2]
        ftplib.connect(host, port)

    # HOST = '127.0.0.1'  # The server's hostname or IP address
    # PORT = 65432        # The port used by the server

   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.connect((HOST, PORT))
       val = input("Send or quit?")
       if(val == "Send" or val == "s"):
           s.sendall(b'1')
           data = s.recv(1024)
       if(val == "Quit" or val == "q"):
           status = 0

   print('Received', repr(data))
