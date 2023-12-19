import socket
import threading
import sys
version = 0.1

#setup server network config
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, 420))
server.listen(1)

#setting up table
table = [['#','#','#'],['#','#','#'],['#','#','#']]
tableChosen = [[False,False,False],[False,False,False],[False,False,False]]

#reset table functionality for new game
def tableReset():
    global table
    global tableChosen
    table = [['#','#','#'],['#','#','#'],['#','#','#']]
    tableChosen = [[False,False,False],[False,False,False],[False,False,False]]

#print table function to output table to both players
def printTable():
    out = ""
    for x in range(3):
        for y in range(3):
            out = out + table[x-1][y-1]
        out = out + "\n"
    return out

#control main game functions, which are player turn as well as displaying the current table to host/guest
def game(client):
    p = 1
    while(True):    
        currTable = printTable()
        client.send(f'{currTable}'.encode('ascii'))
        print(currTable)
        turn(client, p)
        if p == 1:
            p = 0
        else:
            p = 1

#executes the current turn. If host: asks for user input. If Guest: sends message to guest to request input
def turn(client, p):
    if p == 1:
        print("Host Turn:")
        userX, userY = input("Enter row and column (1-3): ").split(" ")
    else:
        client.send(f'Guest Turn:'.encode('ascii'))
        message = client.recv(1024).decode('ascii')
        userX, userY = message.split(" ")
    userX = int(userX)
    userY = int(userY)
    
    if p == 1:
        table[userX-2][userY-2] = 'X'
    else:
        table[userX-2][userY-2] = 'O'

    result = checkGame(table)
    if result == "p1":
        print("You win!")
        client.send(f'EXITP1'.encode('ascii'))
        input("Press ENTER to exit")
        exit()
    if result == "p2":
        print("You Lose!")
        client.send(f'EXITP2'.encode('ascii'))
        input("Press ENTER to exit")
        exit()

#CheckGame will run after every turn to see if the Host/Guest has 3 in a row
def checkGame(table):
    for x in table:
        if (x[0] == x[1]) and (x[1] == x[2]):
            if(x[0] == 'X'):
                return "p1"
            if(x[0] == "O"):
                return "p2"

#connection handler
def conn():
    while(True):
        client, address = server.accept()
        print("Connected to P2")
        client.send(f'Connected to P1'.encode('ascii'))
        game(client)
        


#main
print("Welcome to PyTicTac " + str(version))
print("Starting up connection...")
print("Ask guest to enter in these details: ")
print("IP: " + str(host))
print("Port: 420")

conn()
