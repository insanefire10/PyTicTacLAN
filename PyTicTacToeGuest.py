import socket
import threading
import sys
version = 0.1



host = input("Welcome to PyTicTac! Enter the host IP: ")
port = input("Enter the host port: ")
port = int(port)
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
except:
    print("Connection failed, please ENTER to exit")
    dummy = input("")
    exit()



def receive():
    while(True):
        try:
            message = client.recv(1024).decode('ascii')
            if message == "Guest Turn:":
                print("Guest Turn")
                GuestTurn = input("Enter row and column (1-3): ")
                sendCoordinate(GuestTurn)
                continue
            elif message == "EXITP1":
                print("You Lose!")
                input("Press ENTER to exit")
                exit()
            elif message == "EXITP2":
                print("You Win!")
                input("Press ENTER to exit")
                exit()
            print(message)
        except:
            print("ERROR")
            client.close()
            exit()

def sendCoordinate(GuestTurn):
    client.send(f'{GuestTurn}'.encode('ascii'))

receive()


