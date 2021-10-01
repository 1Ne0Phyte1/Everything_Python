import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(4)

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientSocket.send(bytes("Welcome to the Server", "utf-8"))
    clientSocket.close()