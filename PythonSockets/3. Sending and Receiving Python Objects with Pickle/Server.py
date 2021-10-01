import socket
import time
import pickle


HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(4)

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established")

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)
    #print(msg)

    msg = bytes(f'{len(msg):{HEADERSIZE}}',"utf-8")+ msg

    clientSocket.send(msg)

